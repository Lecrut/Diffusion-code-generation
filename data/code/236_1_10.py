class Square:
    def __init__(self, size):
        self.size = size

    @staticmethod
    def generate_grid(rows, cols):
        grid = []
        for _ in range(rows):
            row = [Square(size) for size in range(1, cols + 1)]
            grid.append(row)
        return grid

if __name__ == '__main__':
    square = Square(5)
    grid = square.generate_grid(3, 4)
    print(grid)