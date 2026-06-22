import matplotlib.pyplot as plt
import numpy as np

COLORGRID_SIZE = 10
COLORMAP_NAME = 'viridis'

def generate_color_grid(size, colormap):
    grid = np.linspace(0, 1, size)
    colors = plt.get_cmap(colormap)(grid)
    return colors.reshape((size, size))

if __name__ == '__main__':
    color_grid = generate_color_grid(COLORGRID_SIZE, COLORMAP_NAME)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(color_grid, interpolation='nearest')
    ax.axis('off')
    plt.show()