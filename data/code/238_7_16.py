import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def add_yellow_box(axes):
    rect = Rectangle((0, 0), 10, 10, color='yellow')
    axes.add_patch(rect)

if __name__ == '__main__':
    fig, ax = plt.subplots()
    add_yellow_box(ax)
    plt.show()