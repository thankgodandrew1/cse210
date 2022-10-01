#The player starts the game with 300 points.
#Individual cards are represented as a number from 1 to 13.
#The current card is displayed.
#The player guesses if the next one will be higher or lower.
#Then the next card is displayed.
#The player earns 100 points if they guessed correctly.
#The player loses 75 points if they guessed incorrectly.
#If a player reaches 0 points the game is over.
#If a player has more than 0 points they decide if they
import random
class Dealer:
    '''The Hilo game dealer, a person who directs the game and also displays result
        Attributes: 
            is_playing (boolean): Whether or not the game is being played.
            previous_card (int): Holds and displays the current card number
            next_card (int): Holds and displays the next card digit to players
            starting_point (int): Holds the initial point which is equal to 300 displays the total points rersults based on users choice'''
    
    def __init__(self):
        """Constructs a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.is_playing = True
        self.previous_card = 0
        self.next_card = 0
        self.starting_point = 300


    def start_game(self):
        """Starts the game by running the main game loop. End game if players point is low.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        while self.is_playing:
            self.individual_cards()
            self.player_guess()
            if self.starting_point == 25 or self.starting_point <=0: 
             break
            self.play_again()
        while self.starting_point == 25 or self.starting_point <=0: 
            print("Oops you don't have enough points to continue the game. Game Over!")
            break
       
    def individual_cards(self):
        """Displays the current card.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        if not self.is_playing:
            return
        cards = random.randint(1 , 13)
        self.previous_card = cards
        print(f'\nThe current card is {self.previous_card}')
        return self.previous_card
        
    def player_guess(self):
        """Asks users guessing choice, determines result based on users decision
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        if self.is_playing:
            guess = (input("Is your guess higher or lower(h/l):"))
            cards1 = random.randint(1 , 13)
            self.next_card = cards1
            if guess == "h":
                if self.next_card > self.previous_card:
                    self.starting_point += 100
                else:
                    self.starting_point -= 75
            elif guess == "l":
                if self.next_card < self.previous_card:
                    self.starting_point += 100
                else:
                    self.starting_point -= 75
            else:
                print('\nOops wrong choice, choose between [h/l]')
                return False

            print(f'Next card was: {self.next_card}')
            print(f'Current score is: {self.starting_point}')

    def play_again(self):
        """Ask users if they want to play again.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        replay = input('Play again [y/n] ')
        self.is_playing = replay == 'y' 
        print()
        