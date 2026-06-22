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
    square = Square(5)
    grid = square.generate_grid(3, 4)
    print(grid)