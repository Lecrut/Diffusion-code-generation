import matplotlib.pyplot as plt

class IsoscelesTrianglePlotter:
    def __init__(self, vertices):
        self.vertices = vertices
    
    @staticmethod
    def default_vertices():
        return [(0, 0), (4, 0), (2, 3)]
    
    def plot_triangle(self):
        x_coords, y_coords = zip(*self.vertices)
        plt.plot(x_coords + (x_coords[0],), y_coords + (y_coords[0],), 'b-')
        plt.fill(x_coords, y_coords, 'g', alpha=0.5)
        plt.axis('equal')
        plt.show()

if __name__ == '__main__':
    plotter = IsoscelesTrianglePlotter(IsoscelesTrianglePlotter.default_vertices())
    plotter.plot_triangle()