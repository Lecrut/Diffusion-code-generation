class Checkerboard:

    def __init__(self):
        self.state = tuple('BWBWBWBW' * 8)

    def get_cell_color(self, x, y):
        index = y * 8 + x
        return self.state[index]
if __name__ == '__main__':
    cb = Checkerboard()
    print(cb.get_cell_color(0, 0))
    print(cb.get_cell_color(1, 1))
    print(cb.get_cell_color(7, 7))