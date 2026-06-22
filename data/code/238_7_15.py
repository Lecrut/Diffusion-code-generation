import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class BoxDrawer:
    def __init__(self, ax):
        self.ax = ax
    
    @staticmethod
    def create_rectangle():
        return Rectangle((0, 0), 10, 10, color='yellow')
    
    def add_box(self):
        rect = self.create_rectangle()
        self.ax.add_patch(rect)

if __name__ == '__main__':
    fig, ax = plt.subplots()
    drawer = BoxDrawer(ax)
    drawer.add_box()
    plt.show()