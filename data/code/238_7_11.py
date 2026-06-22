import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class BoxDrawer:
    def __init__(self, ax):
        self.ax = ax
    
    def add_yellow_box(self):
        rect = Rectangle((0, 0), 10, 10, color='yellow')
        self.ax.add_patch(rect)

if __name__ == '__main__':
    fig, ax = plt.subplots()
    drawer = BoxDrawer(ax)
    drawer.add_yellow_box()
    plt.show()