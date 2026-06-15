class SquareGrid:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
    def populate(self, char):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = char
if __name__ == '__main__':
    grid_size = 5
    my_grid = SquareGrid(grid_size)
    my_grid.populate('#')
    print("Populated Grid:")
    for row in my_grid.grid:
        print("".join(row))