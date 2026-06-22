import itertools

class Checkerboard:
    def __init__(self, size):
        self.size = size
        self.board = self._create_board()

    def _create_board(self):
        return [[(i + j) % 2 for j in range(self.size)] for i in range(self.size)]

    def get_row(self, index):
        return self.board[index]

    def get_column(self, index):
        return [row[index] for row in self.board]

if __name__ == '__main__':
    size = 8
    checkerboard = Checkerboard(size)
    print("Checkerboard:")
    for row in checkerboard.get_row(0):
        print(row)
    print("Column 1:", checkerboard.get_column(1))