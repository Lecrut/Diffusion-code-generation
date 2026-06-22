class SquareGrid:
    def __init__(self, side_length):
        self.side_length = side_length
        self.grid = [[0] * side_length for _ in range(side_length)]

    def set_cell(self, row, col, value):
        if 0 <= row < self.side_length and 0 <= col < self.side_length:
            self.grid[row][col] = value

    def get_cell(self, row, col):
        if 0 <= row < self.side_length and 0 <= col < self.side_length:
            return self.grid[row][col]
        return None

    @staticmethod
    def print_grid(grid):
        for row in grid:
            print(" ".join(str(cell) for cell in row))

if __name__ == '__main__':
    sample_side = 3
    square_grid = SquareGrid(sample_side)
    square_grid.set_cell(0, 0, 1)
    square_grid.set_cell(1, 1, 2)
    square_grid.set_cell(2, 2, 3)
    SquareGrid.print_grid(square_grid.grid)