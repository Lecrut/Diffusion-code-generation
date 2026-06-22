class SquareGrid:

    def __init__(self, side):
        if not isinstance(side, int) or side <= 0:
            raise ValueError('Side length must be a positive integer')
        self.side = side
        self.grid = [[None] * side for _ in range(side)]

    def set_cell(self, row, col, value):
        if not (0 <= row < self.side and 0 <= col < self.side):
            raise IndexError('Row or column out of bounds')
        self.grid[row][col] = value

    def get_cell(self, row, col):
        if not (0 <= row < self.side and 0 <= col < self.side):
            raise IndexError('Row or column out of bounds')
        return self.grid[row][col]
if __name__ == '__main__':
    grid = SquareGrid(3)
    grid.set_cell(0, 1, 'X')
    grid.set_cell(1, 2, 'O')
    print(grid.get_cell(0, 1))
    print(grid.get_cell(1, 2))