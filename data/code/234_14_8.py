class Checkerboard:
    SIZE = 8
    COLORS = ('B', 'W')

    def __init__(self):
        self.state = tuple(self.COLORS[(i + j) % 2] for i in range(self.SIZE) for j in range(self.SIZE))

    def get_cell_color(self, x, y):
        return self.state[x * self.SIZE + y]

if __name__ == '__main__':
    cb = Checkerboard()
    print(cb.get_cell_color(0, 0))
    print(cb.get_cell_color(1, 1))
    print(cb.get_cell_color(7, 7))