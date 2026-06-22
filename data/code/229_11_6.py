import numpy as np

class GridGenerator:
    @staticmethod
    def create_square_grid(size):
        return np.fromfunction(lambda i, j: (i + j) % 2, (size, size))

if __name__ == '__main__':
    grid = GridGenerator.create_square_grid(5)
    print(grid)