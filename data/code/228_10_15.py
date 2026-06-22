import matplotlib.pyplot as plt

class TrianglePlotter:
    VERTEX1 = (0, 0)
    VERTEX2 = (4, 0)
    VERTEX3 = (2, 3)

    @staticmethod
    def get_triangle_vertices():
        return [TrianglePlotter.VERTEX1, TrianglePlotter.VERTEX2, TrianglePlotter.VERTEX3]

    def plot_triangle(self):
        vertices = self.get_triangle_vertices()
        x_coords, y_coords = zip(*vertices)
        plt.figure()
        plt.plot(x_coords + (x_coords[0],), y_coords + (y_coords[0],), 'b-')
        plt.fill(x_coords, y_coords, 'r', alpha=0.5)
        plt.axis('equal')
        plt.title('Isosceles Triangle')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    plotter = TrianglePlotter()
    plotter.plot_triangle()