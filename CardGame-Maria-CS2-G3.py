#Maria AL-Ma'amri - CS2-G3

import random

# فئة تمثل ورقة اللعب
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        return f"{self.rank} of {self.suit}"

# فئة تمثل مجموعة الأوراق
class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Deck.suits for rank in Deck.ranks]
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop()

# فئة تمثل يد اللعب لكل لاعب
class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def remove_card(self, card):
        self.cards.remove(card)
    
    def __repr__(self):
        return ', '.join(str(card) for card in self.cards)

# فئة تمثل لاعب
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.score = 0
    
    def draw_card(self, deck):
        self.hand.add_card(deck.draw())
    
    def play_card(self, card):
        self.hand.remove_card(card)
        return card

# فئة تمثل لعبة الباصرة
class BasraGame:
    def __init__(self, num_players=4):
        self.deck = Deck()
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.current_player_index = 0
        self.table_cards = []
        self.start_game()
    
    def start_game(self):
        # توزيع الأوراق
        for _ in range(4):  # لكل لاعب 4 أوراق
            for player in self.players:
                player.draw_card(self.deck)
        
        # توزيع الأوراق على الطاولة
        for _ in range(4):
            self.table_cards.append(self.deck.draw())
    
    def player_turn(self, player):
        print(f"{player.name}'s turn. Hand: {player.hand}")
        card_to_play = player.hand.cards[0]  #يلعب اللاعب أول ورقة من يده
        print(f"{player.name} plays {card_to_play}")
        played_card = player.play_card(card_to_play)
        self.table_cards.append(played_card)
    
    def play_game(self):
        rounds = 0
        while self.deck.cards or any(player.hand.cards for player in self.players):
            current_player = self.players[self.current_player_index]
            self.player_turn(current_player)
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            rounds += 1
            if rounds > 10:  # عدد الأدوار التقديري لتجنب حلقة لا تنتهي
                break

        # إعلان النتيجة
        self.declare_winner()
    
    def declare_winner(self):
         #حساب النقاط
        for player in self.players:
            player.score = len(player.hand.cards)  # حساب النقاط بناءً على عدد الأوراق المتبقية
        winner = max(self.players, key=lambda p: p.score)
        print(f"{winner.name} wins with {winner.score} points!")

# تشغيل اللعبة
if __name__ == "__main__":
    game = BasraGame()
    game.play_game()
    