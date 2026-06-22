class StarGrid:
    def __init__(self, size):
        self.size = size

    def get_row(self, index):
        return '*' * self.size

    def print_grid(self):
        for i in range(self.size):
            print(self.get_row(i))

if __name__ == '__main__':
    grid = StarGrid(10)
    grid.print_grid()
    print(len(grid.get_row(5)))