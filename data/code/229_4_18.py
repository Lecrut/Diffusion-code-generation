class SquareGrid:
    def __init__(self, side_length):
        self.side_length = side_length
        self.grid = [[0 for _ in range(side_length)] for _ in range(side_length)]

    def set_value(self, row, col, value):
        if 0 <= row < self.side_length and 0 <= col < self.side_length:
            self.grid[row][col] = value

    def get_value(self, row, col):
        if 0 <= row < self.side_length and 0 <= col < self.side_length:
            return self.grid[row][col]
        return None

if __name__ == '__main__':
    sample_grid = SquareGrid(3)
    sample_grid.set_value(1, 1, 42)
    print(sample_grid.get_value(1, 1))