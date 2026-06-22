import matplotlib.pyplot as plt
import numpy as np

def create_grid():
    fig, ax = plt.subplots()
    colors = [
        'red', 'green', 'blue', 'yellow', 'cyan',
        'magenta', 'black', 'white', 'gray', 'orange'
    ]
    grid = np.array(colors * 10).reshape(10, 10)
    ax.imshow(grid, interpolation='nearest')
    plt.show()

if __name__ == '__main__':
    create_grid()