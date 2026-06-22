import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def add_yellow_box(ax):
    if not isinstance(ax, plt.Axes):
        raise ValueError("The provided argument must be an instance of plt.Axes")
    
    rect = Rectangle((0, 0), 10, 10, color='yellow')
    ax.add_patch(rect)

if __name__ == '__main__':
    fig, ax = plt.subplots()
    add_yellow_box(ax)
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    plt.show()