class Square:
    def __init__(self, size):
        self.size = size

    def generate_grid(self, rows, cols):
        grid = []
        for _ in range(rows):
            row = [Square(self.size) for _ in range(cols)]
            grid.append(row)
        return grid

if __name__ == '__main__':
    square_size = 5
    rows = 3
    cols = 4
    square = Square(square_size)
    grid = square.generate_grid(rows, cols)
    print(grid)