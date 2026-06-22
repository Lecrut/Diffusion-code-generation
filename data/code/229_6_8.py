class GridGenerator:
    def __init__(self, size):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]

    def generate_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = i + j

    def print_grid(self):
        for row in self.grid:
            print(row)

if __name__ == '__main__':
    generator = GridGenerator(20)
    generator.generate_grid()
    generator.print_grid()