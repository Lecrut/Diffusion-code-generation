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
    sample_grid = SquareGrid(3)
    sample_grid.set_cell(0, 0, 'X')
    sample_grid.set_cell(1, 1, 'O')
    sample_grid.set_cell(2, 2, '#')

    for row in sample_grid.grid:
        print(" ".join(str(cell) if cell is not None else '.' for cell in row))