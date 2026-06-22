class Square:
    def __init__(self, size):
        self.size = size

    def validate_input(self, rows, cols):
        if not isinstance(rows, int) or not isinstance(cols, int):
            raise ValueError("Rows and columns must be integers.")
        if rows <= 0 or cols <= 0:
            raise ValueError("Rows and columns must be greater than zero.")

    def generate_grid(self, rows, cols):
        self.validate_input(rows, cols)
        grid = []
        for _ in range(rows):
            row = [Square(self.size) for _ in range(cols)]
            grid.append(row)
        return grid

if __name__ == '__main__':
    square = Square(5)
    grid = square.generate_grid(3, 4)
    print(grid)