import itertools

class Checkerboard:
    def __init__(self, size):
        self.size = size
        self.board = self._create_checkerboard()

    def _create_checkerboard(self):
        return [[(i + j) % 2 for j in range(self.size)] for i in range(self.size)]

    def get_board(self):
        return self.board

if __name__ == '__main__':
    checkerboard_instance = Checkerboard(8)
    print(checkerboard_instance.get_board())