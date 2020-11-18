INSTRUCTIONS = """\n | Welcome to our version of the Blackjack Game |
=================================================================================
The goal is to get as close to 21 as possible, without going over 21. 
Each card has a value and a suit. The values are added for the final result.

The game starts by dealing two cards to the player (you) and to the dealer.            
You are playing against the dealer. On each turn, you must choose if you
would like to take another card or stand to stop the game and see if you won.

The game ends if the total value of the player's hand goes over 21,
and if the total value of the hand is below 21, the game continues
until the player chooses to stand.

When the game ends or when the player chooses to stand,
the total value of each hand is calculated.  
The value that is closest to 21 without going over it wins the game.
If the total value is over 21, the player or dealer automatically lose the game.
=================================================================================
"""
import random

class Card:
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def get_suit(self):
        return self._suit
    def get_value(self):
        return self._value

    def show(self):
        print(f'{self._value} of {self._suit}.')

class Deck:
    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    def __init__(self):
        self._cards = []
        self.build()

    def build(self):
        for suit in Deck.suits:
            for value in range(1, 12):
                self._cards.append(Card(suit, value))

    def show(self):
        for card in self._cards:
            card.show()

    def shuffle(self):  # Fisher-Yates
        for i in range(len(self._cards)-1, 0, -1):
            # Pick a random index from 0 to i
            rand = random.randint(0, i)
            # Swap arr[i] with the element at random index
            self._cards[i],self._cards[rand] = self._cards[rand],self._cards[i]

    def draw(self):
        if self._cards:
            return self._cards.pop()

class Player:
    def __init__(self, name, is_dealer=False):
        self._name = name
        self._hand = []
        self._is_dealer = is_dealer

    def get_name(self):
        return self._name
    def get_is_dealer(self):
        return self._is_dealer

    def draw(self, deck):
        self._hand.append(deck.draw())
        return self

    def show_hand(self, reveal_card=False):
        if not self._is_dealer:
            for card in self._hand:
                card.show()
            else:
                for i in range(len(self._hand)-1):
                    self._hand[i].show()
                if reveal_card:
                    self._hand[-1].show()
                else:
                    print('X')

    def discard(self):
        return self._hand.pop()

    def get_hand_value(self):
        value = 0
        for card in self._hand:
            value += card._value
        return value

class CardGame:  # Main game logic class
    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.start_game()

    def start_game(self):
        print(INSTRUCTIONS)
        turn = 1
        # Shuffle the deck
        self.deck.shuffle()
        # Draw two cards
        self.player.draw(self.deck).draw(self.deck)
        self.dealer.draw(self.deck).draw(self.deck)
        while True:
            print(f'Turn #{turn}')
            print(f'The dealers hand is:')
            self.dealer.show_hand()
            print('Your hand is:')
            self.player.show_hand()
            if self.player.get_hand_value() > 21:
                print('Your total hand is over 21')
                break
            elif self.player.get_hand_value() == 21:
                print('Player Wins')
                break

            choice = self.ask_choice()  # 1 draw, 2 stay
            turn += 1
            if choice  == 1:
                self.player.draw(self.deck)
            else:
                break
            player_hand = self.player.get_hand_value()
            print(f'Value - your hand: {player_hand}')
            dealer_hand = self.dealer.get_hand_value()
            print(f'Value - dealers hand: {dealer_hand}')
            print(f'The dealers hand was:')
            self.dealer.show_hand(True)

            if player_hand > 21:
                print(f'You lose {self.player._name}')
            elif dealer_hand > 21 or player_hand == 21 or player_hand > dealer_hand:
                print(f'You win {self.player._name} with {player_hand} vs. {dealer_hand}')
            elif player_hand < dealer_hand:
                print(f'You lose {self.player._name} with {player_hand} vs. {dealer_hand} ')
            else:
                print(f'We have a tie with {dealer_hand} points.')

    def ask_choice(self):
        print('What do you want to do:')
        print('1 - Ask for another card')
        print('2 - Stand')
        choice = int(input('Please enter your choice (1 or 2) below:'))
        if choice == 1 or choice == 2:
            return choice
        else:
            print('Input not valid --> you will stand for now.')
            return 2

# Run Game
deck = Deck()
you = Player('Patxi')
dealer = Player('Dealer', True)

game = CardGame(deck, you, dealer)



