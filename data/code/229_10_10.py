import matplotlib.pyplot as plt
import numpy as np

def generate_color_grid():
    grid = np.linspace(0, 1, 10)
    colors = plt.cm.viridis(grid)
    return colors.reshape((10, 10))

if __name__ == '__main__':
    color_grid = generate_color_grid()
    fig, ax = plt.subplots()
    ax.imshow(color_grid, interpolation='nearest')
    plt.show()