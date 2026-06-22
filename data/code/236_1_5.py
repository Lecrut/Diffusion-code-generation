class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def generate_grid(self, rows, cols):
        grid = []
        for _ in range(rows):
            row = [Square(self.side_length) for _ in range(cols)]
            grid.append(row)
        return grid

if __name__ == '__main__':
    square = Square(5)
    grid = square.generate_grid(3, 4)
    print(grid)