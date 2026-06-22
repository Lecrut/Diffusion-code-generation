import matplotlib.pyplot as plt

def create_grid():
    fig, ax = plt.subplots()
    colors = [
        ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white', 'black', 'gray', 'orange'],
        ['green', 'blue', 'yellow', 'cyan', 'magenta', 'white', 'black', 'gray', 'orange', 'red'],
        ['blue', 'yellow', 'cyan', 'magenta', 'white', 'black', 'gray', 'orange', 'red', 'green'],
        ['yellow', 'cyan', 'magenta', 'white', 'black', 'gray', 'orange', 'red', 'green', 'blue'],
        ['cyan', 'magenta', 'white', 'black', 'gray', 'orange', 'red', 'green', 'blue', 'yellow'],
        ['magenta', 'white', 'black', 'gray', 'orange', 'red', 'green', 'blue', 'yellow', 'cyan'],
        ['white', 'black', 'gray', 'orange', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta'],
        ['black', 'gray', 'orange', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white'],
        ['gray', 'orange', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white', 'black'],
        ['orange', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white', 'black', 'gray']
    ]
    for i in range(10):
        for j in range(10):
            ax.add_patch(plt.Rectangle((i, 9-j), 1, 1, color=colors[i][j]))
    plt.xlim(-0.5, 10.5)
    plt.ylim(-0.5, 10.5)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    create_grid()