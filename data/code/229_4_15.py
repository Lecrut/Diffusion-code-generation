class SquareGrid:
    def __init__(self, side):
        if not isinstance(side, int) or side <= 0:
            raise ValueError("Side must be a positive integer")
        self.side = side
        self.grid = [[None] * side for _ in range(side)]

    def set_cell(self, row, col, value):
        if not (0 <= row < self.side and 0 <= col < self.side):
            raise IndexError("Row and column indices must be within the grid dimensions")
        self.grid[row][col] = value

    def get_cell(self, row, col):
        if not (0 <= row < self.side and 0 <= col < self.side):
            raise IndexError("Row and column indices must be within the grid dimensions")
        return self.grid[row][col]

if __name__ == '__main__':
    grid = SquareGrid(3)
    grid.set_cell(0, 0, 'X')
    grid.set_cell(1, 1, 'O')
    grid.set_cell(2, 2, 'X')

    print("Cell at (0, 0):", grid.get_cell(0, 0))
    print("Cell at (1, 1):", grid.get_cell(1, 1))
    print("Cell at (2, 2):", grid.get_cell(2, 2))