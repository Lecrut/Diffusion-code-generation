class GridGenerator:
    SIZE = 5

    @staticmethod
    def generate_grid():
        return [[(i, j) for j in range(GridGenerator.SIZE)] for i in range(GridGenerator.SIZE)]

if __name__ == '__main__':
    grid = GridGenerator.generate_grid()
    print(grid)