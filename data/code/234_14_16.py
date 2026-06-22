class Checkerboard:
    def __init__(self):
        self.state = tuple('B' if (i + j) % 2 == 0 else 'W' for i in range(8) for j in range(8))

    def get_cell(self, x, y):
        return self.state[x * 8 + y]

if __name__ == '__main__':
    board = Checkerboard()
    print(board.get_cell(1, 2))