class SquareGrid:
    def __init__(self, size):
        self.size = size
    def populate_and_print(self, char='.'):
        grid = []
        for i in range(self.size):
            row = [char] * self.size
            grid.append(row)
        for row in grid:
            print("".join(row))
if __name__ == '__main__':
    grid1 = SquareGrid(5)
    grid1.populate_and_print()
    grid2 = SquareGrid(8)
    grid2.populate_and_print()