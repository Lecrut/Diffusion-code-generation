class Checkerboard:
    def __init__(self, size=8):
        self.size = size
        self.state = tuple(('B' if (i + j) % 2 == 0 else 'W' for i in range(size) for j in range(size)))

    def get_cell_color(self, x, y):
        return self.state[x * self.size + y]

if __name__ == '__main__':
    cb = Checkerboard()
    print(cb.get_cell_color(0, 0))
    print(cb.get_cell_color(1, 1))
    print(cb.get_cell_color(7, 7))