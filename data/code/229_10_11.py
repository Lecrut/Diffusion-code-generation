import matplotlib.pyplot as plt
import numpy as np

class ColorGridGenerator:
    def __init__(self, size=10):
        self.size = size
        self.grid = None

    def generate_grid(self):
        grid_values = np.linspace(0, 1, self.size * self.size)
        self.grid = grid_values.reshape((self.size, self.size))

    def display_grid(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        cax = ax.matshow(self.grid, cmap='viridis')
        fig.colorbar(cax)
        ax.axis('off')
        plt.show()

if __name__ == '__main__':
    generator = ColorGridGenerator(10)
    generator.generate_grid()
    generator.display_grid()