class SquareGrid:
    def __init__(self, side_length):
        if not isinstance(side_length, int) or side_length <= 0:
            raise ValueError("Side length must be a positive integer")
        self.side_length = side_length
        self.grid = [[None] * side_length for _ in range(side_length)]

    def set_cell(self, row, col, value):
        if not (0 <= row < self.side_length and 0 <= col < self.side_length):
            raise IndexError("Row and column indices must be within the grid bounds")
        self.grid[row][col] = value

    def get_cell(self, row, col):
        if not (0 <= row < self.side_length and 0 <= col < self.side_length):
            raise IndexError("Row and column indices must be within the grid bounds")
        return self.grid[row][col]

if __name__ == '__main__':
    sample_side = 5
    square_grid = SquareGrid(sample_side)
    square_grid.set_cell(2, 3, 'X')
    print(square_grid.get_cell(2, 3))