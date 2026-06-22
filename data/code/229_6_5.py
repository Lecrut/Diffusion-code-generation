class SumGridGenerator:
    GRID_SIZE = 20

    @staticmethod
    def generate_grid():
        grid = [[0] * SumGridGenerator.GRID_SIZE for _ in range(SumGridGenerator.GRID_SIZE)]
        for i in range(SumGridGenerator.GRID_SIZE):
            for j in range(SumGridGenerator.GRID_SIZE):
                grid[i][j] = i + j
        return grid

if __name__ == '__main__':
    sample_grid = SumGridGenerator.generate_grid()
    print(sample_grid)