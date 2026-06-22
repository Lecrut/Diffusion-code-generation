import matplotlib.pyplot as plt

def create_checkerboard():
    fig, ax = plt.subplots()
    for i in range(8):
        for j in range(8):
            color = 'black' if (i + j) % 2 == 0 else 'white'
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color))
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    create_checkerboard()