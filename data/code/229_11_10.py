import numpy as np

class GridGenerator:
    def __init__(self, size):
        self.size = size

    def generate_grid(self):
        return np.fromfunction(lambda i, j: (i + j) % 2, (self.size, self.size))

if __name__ == '__main__':
    grid_gen = GridGenerator(5)
    result = grid_gen.generate_grid()
    print(result)