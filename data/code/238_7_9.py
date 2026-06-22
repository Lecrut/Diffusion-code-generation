import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def create_yellow_box(ax):
    rect = Rectangle((0, 0), 10, 10, color='yellow')
    ax.add_patch(rect)

def validate_ax(ax):
    if not isinstance(ax, plt.Axes):
        raise ValueError("The provided argument must be a matplotlib.axes.Axes object.")

if __name__ == '__main__':
    fig, ax = plt.subplots()
    validate_ax(ax)
    create_yellow_box(ax)
    plt.show()