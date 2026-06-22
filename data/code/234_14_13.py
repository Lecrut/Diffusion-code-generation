class Checkerboard:
    def __init__(self, rows=8, cols=8, char1='X', char2='O'):
        if not (rows > 0 and cols > 0):
            raise ValueError("Rows and columns must be greater than zero.")
        self.rows = rows
        self.cols = cols
        self.state = tuple((char1 if (i + j) % 2 == 0 else char2 for i in range(rows) for j in range(cols)))

    def get_cell_color(self, x, y):
        if not (0 <= x < self.rows and 0 <= y < self.cols):
            raise ValueError("Coordinates must be within the bounds of the checkerboard.")
        return self.state[x * self.cols + y]

if __name__ == '__main__':
    cb = Checkerboard(5, 7, 'X', 'O')
    print(cb.get_cell_color(0, 0))
    print(cb.get_cell_color(1, 1))
    print(cb.get_cell_color(4, 6))