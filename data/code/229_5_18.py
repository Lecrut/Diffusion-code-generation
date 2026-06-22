import numpy as np

class GridGenerator:
    def __init__(self, size):
        self.size = size

    def generate_grid(self):
        return np.arange(self.size**2).reshape(self.size, self.size)

if __name__ == '__main__':
    generator = GridGenerator(4)
    grid = generator.generate_grid()
    print(grid)