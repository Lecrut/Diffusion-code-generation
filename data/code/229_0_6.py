import matplotlib.pyplot as plt
import numpy as np

def create_grid():
    fig, ax = plt.subplots()
    colors = [
        'red', 'blue', 'green', 'yellow', 'cyan',
        'magenta', 'white', 'black', 'gray', 'orange'
    ]
    grid_data = np.tile(colors, (10, 10))
    im = ax.imshow(grid_data)
    plt.show()

if __name__ == '__main__':
    create_grid()