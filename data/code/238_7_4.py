import matplotlib.pyplot as plt

def add_yellow_box(ax):
    rect = plt.Rectangle((0, 0), 10, 10, color='yellow')
    ax.add_patch(rect)

if __name__ == '__main__':
    fig, ax = plt.subplots()
    add_yellow_box(ax)
    plt.show()