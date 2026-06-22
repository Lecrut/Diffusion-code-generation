import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def add_yellow_box(ax):
    rect = Rectangle((0, 0), 10, 10, color='yellow')
    ax.add_patch(rect)

if __name__ == '__main__':
    fig, ax = plt.subplots()
    add_yellow_box(ax)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)
    plt.show()