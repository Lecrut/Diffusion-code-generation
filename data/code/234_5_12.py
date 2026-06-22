import itertools

class Checkerboard:
    def __init__(self, size):
        self.size = size
        self.board = self._create_checkerboard()

    def _create_checkerboard(self):
        return [[(i + j) % 2 for j in range(self.size)] for i in range(self.size)]

    def print_board(self):
        for row in self.board:
            print(' '.join(str(cell) for cell in row))

if __name__ == '__main__':
    cb = Checkerboard(8)
    cb.print_board()