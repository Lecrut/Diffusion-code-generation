import numpy as np

BOARD_SIZE = 8
COLOR_BLACK = 'B'
COLOR_WHITE = 'W'

class Checkerboard:
    def __init__(self):
        self.state = tuple(COLOR_BLACK if (i + j) % 2 == 0 else COLOR_WHITE for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

    def get_cell_color(self, x, y):
        return self.state[x * BOARD_SIZE + y]

if __name__ == '__main__':
    cb = Checkerboard()
    print(cb.get_cell_color(0, 0))
    print(cb.get_cell_color(1, 1))
    print(cb.get_cell_color(7, 7))