class Checkerboard:
    def __init__(self):
        self.state = tuple(('B' if (i + j) % 2 == 0 else 'W' for i in range(8) for j in range(8)))

    def get_cell_color(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Coordinates must be integers.")
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            raise ValueError("Coordinates out of bounds. Must be between 0 and 7.")
        return self.state[x * 8 + y]

if __name__ == '__main__':
    cb = Checkerboard()
    print(cb.get_cell_color(0, 0))
    print(cb.get_cell_color(3, 4))
    print(cb.get_cell_color(7, 7))