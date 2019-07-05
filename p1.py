import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

# player


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Random player
class RandomPlayer(Player):
    def move(self):
        moves = ['rock', 'paper', 'scissors']
        return random.choice(moves)


# Human player
class HumanPlayer(Player):
    def move(self):
        isCorrect = False
        Answer = "Not Today"
        Answer = input("rock , paper , scissors ?")
        if Answer == 'rock' or Answer == 'paper' or Answer == 'scissors':
            isCorrect = True
        else:
            while isCorrect is False:
                Answer = input("rock , paper , scissors ?")
                if Answer == 'rock' or Answer == 'paper' or Answer == 'scissors':
                    isCorrect = True
                    return Answer


# A player that cycles through the three moves
class cyclePlayer(Player):
    def __init__(self):
        self.counter = 0

    def move(self):
        moves = ['rock', 'paper', 'scissors']
        if self.counter == 2:
            self.counter = 0
            return moves[2]
        else:
            self.counter += 1
            return moves[self.counter-1]


class ReflectPlayer(Player):
    def __init__(self):
        self.Round_counter = 0

        def move(self):
            if self.Round_counter == 0:
                Round_counter += 1
                moves = ['rock', 'paper', 'scissors']
                return random.choice(moves)
            else:
                Round_counter += 1
                return learn(self, name, name2)

        def learn(self, my_move, their_move):
            if self.their_move == 'rock':
                return 'rock'
            if self.their_move == 'paper':
                return 'paper'
            else:
                return 'scissors'


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.Player_1_Counter = 0
        self.Player_2_Counter = 0

    def beats(self):
        player1 = self.p1.move()
        player2 = self.p2.move()
        result = ''
        if player1 == player2:
            result = 'They are equals'
        elif player1 == 'rock' and player2 == 'scissors':
            result = player1
        elif player1 == 'scissors' and player2 == 'paper':
            result = player1
        elif player1 == 'paper' and player2 == 'rock':
            result = player1
        elif player1 == 'scissors' and player2 == 'rock':
            result = player2
        elif player1 == "rock" and player2 == "paper":
            result = player2
        elif player1 == 'paper' and player2 == 'scissors':
            result = player2

        if player1 == player2:
            print("** they are equals **")
            self.Player_1_Counter += 1
            self.Player_2_Counter += 1
        elif result == player1:
            print("** PLAYER ONE WINS **")
            self.Player_1_Counter += 1
        elif result == player2:
            print("** PLAYER TOW WINS **")
            self.Player_2_Counter += 1

    def winner(self):
        self.beats()

        print("Score :\n PlayerOne")

        print(self.Player_1_Counter)

        print ("PlayerTow")

        print(self.Player_2_Counter)

    def Final_massge(self):
        Player_1_Counter = self.Player_1_Counter
        Player_2_Counter = self.Player_2_Counter
        if Player_1_Counter > Player_2_Counter:
            print("player 1 is the Winner Congrats! :)")
        elif Player_1_Counter < Player_2_Counter:
            print("player 2 is the Winner Congrats! :)")
        else:
            print("They are equals :( ")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print("Player 1: " + str(move1) + " Player 2: " + str(move2))

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        print("you played "+str(move1))
        print("opponent played "+str(move2))
        self.winner()
        self.Final_massge()

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print("Round: ")
            print(round)
            self.play_round()
        print("Game over!")

    def choose_how_many_Round(self):
        print("Game Start!")
        for round in range(input("Enter how many Round you wnant to play")):
            print("Round ")
            print(round)
            self.play_round()
        print("Game Over!")


if __name__ == '__main__':
    game = Game(humanPlayer(), humanPlayer())
    game.play_game()
