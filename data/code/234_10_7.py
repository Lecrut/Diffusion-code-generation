import numpy as np

class CheckerboardGenerator:
    def __init__(self, size=8):
        self.size = size
        self.board = None

    def generate_board(self):
        self.board = np.zeros((self.size, self.size), dtype=int)
        for i in range(self.size):
            for j in range(self.size):
                if (i + j) % 2 == 0:
                    self.board[i, j] = 1
        return self.board

    def print_board(self):
        print(self.board)

if __name__ == '__main__':
    checkerboard_generator = CheckerboardGenerator(8)
    checkerboard_generator.generate_board()
    checkerboard_generator.print_board()