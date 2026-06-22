import matplotlib.pyplot as plt

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    @staticmethod
    def create_patch(x1, y1, x2, y2, color='red'):
        return plt.Rectangle((x1, y1), x2 - x1, y2 - y1, color=color)
    
    def draw(self, ax):
        patch = Rectangle.create_patch(self.x1, self.y1, self.x2, self.y2)
        ax.add_patch(patch)

if __name__ == '__main__':
    fig, ax = plt.subplots()
    rect = Rectangle(0, 0, 5, 3)
    rect.draw(ax)
    print(fig)