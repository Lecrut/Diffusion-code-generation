import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def create_yellow_box(ax):
    rect = Rectangle((0, 0), width=10, height=10, color='yellow')
    ax.add_patch(rect)

if __name__ == '__main__':
    fig, ax = plt.subplots()
    create_yellow_box(ax)
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    plt.show()