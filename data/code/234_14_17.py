class Checkerboard:
    SIZE = 8
    BLACK = 'B'
    WHITE = 'W'

    @classmethod
    def generate_state(cls):
        return tuple((cls.BLACK if (i + j) % 2 == 0 else cls.WHITE for i in range(cls.SIZE) for j in range(cls.SIZE)))

    def __init__(self):
        self.state = Checkerboard.generate_state()

    def get_cell_color(self, x, y):
        return self.state[x * Checkerboard.SIZE + y]

if __name__ == '__main__':
    cb = Checkerboard()
    print(cb.get_cell_color(0, 0))
    print(cb.get_cell_color(1, 1))
    print(cb.get_cell_color(7, 7))