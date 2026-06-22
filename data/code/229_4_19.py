class SquareGrid:

    def __init__(self, size):
        if not isinstance(size, int) or size <= 0:
            raise ValueError('Size must be a positive integer')
        self.size = size
        self.grid = [[None] * size for _ in range(size)]

    def set_cell(self, row, col, value):
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise IndexError('Row and column indices must be within the grid bounds')
        self.grid[row][col] = value

    def get_cell(self, row, col):
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise IndexError('Row and column indices must be within the grid bounds')
        return self.grid[row][col]
if __name__ == '__main__':
    sample_size = 3
    grid = SquareGrid(sample_size)
    grid.set_cell(0, 0, 'X')
    grid.set_cell(1, 1, 'O')
    grid.set_cell(2, 2, 'X')
    print(grid.get_cell(0, 0))
    print(grid.get_cell(1, 1))
    print(grid.get_cell(2, 2))