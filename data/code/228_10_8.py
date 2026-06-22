import matplotlib.pyplot as plt

def plot_isosceles_triangle(vertices):
    x_coords, y_coords = zip(*vertices)
    plt.plot(x_coords + (x_coords[0],), y_coords + (y_coords[0],), 'b-')
    plt.fill(x_coords, y_coords, 'blue', alpha=0.5)
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    triangle_vertices = [(0, 0), (4, 0), (2, 3)]
    plot_isosceles_triangle(triangle_vertices)