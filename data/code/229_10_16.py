import matplotlib.pyplot as plt
import numpy as np

class ColorGridGenerator:
    SIZE = 10
    COLORMAP = 'viridis'

    @staticmethod
    def generate_color_grid():
        grid = np.linspace(0, 1, ColorGridGenerator.SIZE)
        colors = plt.cm.get_cmap(ColorGridGenerator.COLORMAP)(grid)
        return colors.reshape((ColorGridGenerator.SIZE, ColorGridGenerator.SIZE))

if __name__ == '__main__':
    color_grid = ColorGridGenerator.generate_color_grid()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(color_grid, interpolation='nearest')
    ax.axis('off')
    plt.show()