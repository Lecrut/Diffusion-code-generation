import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def add_yellow_box(ax):
    rect = Rectangle((0, 0), width=10, height=10, color='yellow')
    ax.add_patch(rect)

if __name__ == '__main__':
    fig, ax = plt.subplots()
    add_yellow_box(ax)
    plt.show()