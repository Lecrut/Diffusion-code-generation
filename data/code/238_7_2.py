import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def draw_box(ax):
    box = Rectangle((0, 0), width=10, height=10, color='yellow')
    ax.add_patch(box)

if __name__ == '__main__':
    fig, axis = plt.subplots()
    draw_box(axis)
    axis.set_xlim(0, 20)
    axis.set_ylim(0, 20)
    plt.show()