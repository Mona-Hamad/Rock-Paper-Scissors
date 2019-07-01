
import random
import time


moves = ['rock', 'paper', 'scissors']


random.choice(moves)

# pause... easy to read:)


def print_time(output):
    print(output)
    time.sleep(0.5)


class Player:
    def __init__(self):
        self.my_move = random.choice(moves)
        self.their_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            Humenchoice = str(
                input("\nChoose 'Rock', 'Paper' or 'Scissors': "))
            Humenchoice_lower = Humenchoice.lower()
            if Humenchoice_lower not in ['rock', 'paper', 'scissors']:
                print("\n I can not understand you !!")
            else:
                break
        return Humenchoice_lower


class ReflectPlayer(Player):

    def move(self):
        return self.their_move


""" I was doubting between these two classes for the cycle player """

# group1 = ['paper', 'scissors']
# group2 = ['rock', 'scissors']
# group3 = ['rock', 'paper']
# class CyclePlayer:

#     def move(self):
#         if self.my_move == "rock":
#             return random.choice(group1)
#         elif self.my_move == "paper":
#             return random.choice(group2)
#         else:
#             return random.choice(group3)
#


class CyclePlayer (Player):

    def move(self):
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def Keep_Score(self, p1, p2):
        if beats(p1, p2):
            self.p1_score = self.p1_score + 1
        elif beats(p2, p1):
            self.p2_score = self.p2_score + 1
        else:
            pass

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        self.Keep_Score(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def final_score(self):
        if self.p1_score > self.p2_score:
            print_time(
                f"\nPlayer 1 wins The Game !!!!"
                f"** {self.p1_score} -- {self.p2_score}**")
        elif self.p1_score < self.p2_score:
            print_time(
                f"\nPlayer 2 wins The Game !!!!"
                f"** {self.p1_score} -- {self.p2_score} **")
        else:
            print_time(
                f"\nIt's a tie!, let's try again"
                f" ** {self.p1_score} -- {self.p2_score} **")

    def play_game(self):
        print("\nGame start!")
        # To avoid the problem when is not int, i used try ,,,,, except here.
        while True:
            try:
                round_to_be_played = (
                    int(input("How many Round do you want to play ??  ")))

                for round in range(round_to_be_played):
                    round += 1
                    print(f"\nRound {round}:")

                    self.play_round()
                    print_time(
                        f"\nScore: Player 1: {self.p1_score}"
                        f" __  Player 2: {self.p2_score}")
                    if self.p1_score > self.p2_score:
                        print_time(
                            f"\nPlayer 1 wins Round ***( {round} ) ***")
                        round_rest = round_to_be_played - round
                        print_time(
                            f"** Remaining Round {round_rest}"
                            f" out of {round_to_be_played} **")
                    elif self.p1_score < self.p2_score:
                        print_time(
                            f"\nPlayer 2 wins Round ***( {round} )*** ")
                        round_rest = round_to_be_played - round
                        print_time(
                            f"** Remaining Round {round_rest}"
                            f" out of {round_to_be_played} **")
                    else:
                        print_time(
                            f"\nIt is a tie in Round ({round})  "
                            f"  *** {self.p1_score} -- {self.p2_score} ***")
                        round_rest = round_to_be_played - round
                        print_time(
                            f"** Remaining Round {round_rest}"
                            f" out of {round_to_be_played} **")

                self.final_score()

                print_time("\nGame over!")
                while True:
                    Play_again = input(
                        "\nDo you want to play again !! (Yes or No) :  ")
                    c = Play_again.lower()
                    if c == "yes":
                        self.p1_score = 0
                        self.p2_score = 0
                        self.play_game()
                    else:
                        break

            except ValueError:
                print("\nPlease enter a number !!")
                continue
            else:
                return round_to_be_played
                break


play_against = {
    "1": Player(),
    "2": RandomPlayer(),
    "3": HumanPlayer(),
    "4": ReflectPlayer(),
    "5": CyclePlayer()}
# To avoid the problem,if the player inputs  not 1,2,3,4,5  not in the
# dic, i used try ,,,,, except here.
while True:
    player_against_choice = input(
        "\nAgainst who do you want to play !!"
        "\n1-Player (always Rock :))\n2-RandomPlayer"
        "\n3-HumanPlayer \n4-ReflectPlayer"
        "\n5-CyclePlayer (Please enter 1,2,...) ")
    try:
        play_against[player_against_choice]
        break
    except KeyError:
        print("\nPleace enter a number !!")

if __name__ == '__main__':
    game = Game((play_against[player_against_choice]), HumanPlayer())
    game.play_game()
