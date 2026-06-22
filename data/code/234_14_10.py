class Checkerboard:
    def __init__(self, rows=8, cols=8):
        self.state = tuple(('B' if (i + j) % 2 == 0 else 'W' for i in range(rows) for j in range(cols)))

    def get_cell_color(self, x, y):
        return self.state[x * cols + y]

if __name__ == '__main__':
    cb = Checkerboard(10, 10)
    print(cb.get_cell_color(3, 4))
    print(cb.get_cell_color(5, 5))
    print(cb.get_cell_color(9, 9))