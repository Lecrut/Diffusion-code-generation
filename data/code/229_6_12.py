class SumGridGenerator:

    def __init__(self, size):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]

    def generate_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = i + j

    def get_grid(self):
        return self.grid
if __name__ == '__main__':
    generator = SumGridGenerator(20)
    generator.generate_grid()
    sample_grid = generator.get_grid()
    print(sample_grid[10][10])