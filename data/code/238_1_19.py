import matplotlib.pyplot as plt

class RectangleDrawer:
    def __init__(self):
        self.ax = plt.subplots()[1]

    @staticmethod
    def calculate_coordinates():
        return (0, 0), (5, 0), (5, 3), (0, 3)

    def draw_rectangle(self):
        coordinates = self.calculate_coordinates()
        self.ax.fill(*zip(*coordinates), 'red')
        return self.ax

if __name__ == '__main__':
    drawer = RectangleDrawer()
    plot_object = drawer.draw_rectangle()
    print(plot_object)