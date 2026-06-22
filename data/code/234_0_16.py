import matplotlib.pyplot as plt

def create_checkerboard():
    fig, ax = plt.subplots()
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = 'white'
            else:
                color = 'black'
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color))
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    create_checkerboard()