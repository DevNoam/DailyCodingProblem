import random


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()

        self.dug = set()

    def make_new_board(self):
        # construction of a new board based on dim_size and num_bombs.
        # generation of a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        #plant the bombs:
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                # this means there is already a bomb there.
                continue

            board[row][col] = "*"
            bombs_planted += 1
        return board
# play the game

def play(dim_size=10,num_bombs=10):
    # step 1: create the board and plant the bombs
    # step 2: show the user the board and ask for where they want to dig
    pass
play()


