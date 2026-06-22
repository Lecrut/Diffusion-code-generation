class MultiplicationGridGenerator:
    ROWS = 10
    COLS = 10

    def generate(self):
        return [[r * c for c in range(1, self.COLS + 1)] for r in range(1, self.ROWS + 1)]

    def get_total_elements(self):
        return self.ROWS * self.COLS

    def get_sum_of_grid(self, grid):
        total = 0
        for row in grid:
            for val in row:
                total += val
        return total

    def get_last_element(self, grid):
        return grid[-1][-1]

if __name__ == '__main__':
    generator = MultiplicationGridGenerator()
    grid = generator.generate()
    print(grid)
    print(generator.get_total_elements())
    print(generator.get_sum_of_grid(grid))
    print(generator.get_last_element(grid))