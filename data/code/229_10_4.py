import matplotlib.pyplot as plt
import numpy as np

def generate_color_grid(size=10):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    
    grid = np.linspace(0, 1, size * size)
    colors = plt.cm.viridis(grid).reshape((size, size))
    return colors

def display_color_grid(colors):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(colors, interpolation='nearest')
    ax.axis('off')
    plt.show()

if __name__ == '__main__':
    try:
        color_grid = generate_color_grid(10)
        display_color_grid(color_grid)
    except ValueError as e:
        print(e)