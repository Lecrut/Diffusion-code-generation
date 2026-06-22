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
    square_size = 5
    grid_rows = 3
    grid_cols = 4
    square = Square(square_size)
    generated_grid = square.generate_grid(grid_rows, grid_cols)
    print(generated_grid)