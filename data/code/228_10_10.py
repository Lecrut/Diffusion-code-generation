import matplotlib.pyplot as plt

class IsoscelesTriangle:
    def __init__(self, vertices):
        self.vertices = vertices

    def plot(self):
        x_coords, y_coords = zip(*self.vertices)
        plt.plot(x_coords + (x_coords[0],), y_coords + (y_coords[0],), 'b-')
        plt.fill(x_coords, y_coords, 'r', alpha=0.5)
        plt.axis('equal')
        plt.title('Isosceles Triangle')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    triangle = IsoscelesTriangle([(0, 0), (4, 0), (2, 3)])
    triangle.plot()