import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def create_yellow_box(ax):
    rect = Rectangle((0, 0), width=10, height=10, color='yellow')
    ax.add_patch(rect)

def validate_ax_object(ax):
    if not isinstance(ax, plt.Axes):
        raise ValueError("The provided object is not a matplotlib Axes instance.")

if __name__ == '__main__':
    fig, ax = plt.subplots()
    validate_ax_object(ax)
    create_yellow_box(ax)
    plt.show()