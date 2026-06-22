class GridGenerator:

    def __init__(self, size):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]

    def generate_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = i + j
if __name__ == '__main__':
    generator = GridGenerator(20)
    generator.generate_grid()
    print(generator.grid[:5])