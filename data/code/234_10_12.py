import numpy as np

class Checkerboard:
    def __init__(self, size=8):
        self.size = size
        self.board = self.generate_board()

    def generate_board(self):
        board = np.zeros((self.size, self.size), dtype=int)
        for i in range(self.size):
            for j in range(self.size):
                if (i + j) % 2 == 0:
                    board[i, j] = 1
        return board

    def get_board(self):
        return self.board

if __name__ == '__main__':
    checkerboard_instance = Checkerboard(8)
    print(checkerboard_instance.get_board())