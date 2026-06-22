import matplotlib.pyplot as plt

def create_square_grid():
    fig, ax = plt.subplots()
    colors = [
        'red', 'green', 'blue', 'yellow', 'cyan',
        'magenta', 'white', 'black', 'gray', 'orange'
    ]
    for i in range(10):
        for j in range(10):
            ax.add_patch(plt.Rectangle((i, j), 1, 1, color=colors[(i + j) % len(colors)]))
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    create_square_grid()