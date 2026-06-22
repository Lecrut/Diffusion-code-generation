import matplotlib.pyplot as plt

def plot_isosceles_triangle():
    vertices = [(0, 0), (4, 0), (2, 3)]
    validate_vertices(vertices)
    x_coords, y_coords = zip(*vertices)
    plot_and_fill(x_coords, y_coords)

def validate_vertices(vertices):
    if len(vertices) != 3:
        raise ValueError("Vertices must consist of exactly three points.")
    for vertex in vertices:
        if len(vertex) != 2:
            raise ValueError("Each vertex must be a pair of coordinates.")

def plot_and_fill(x_coords, y_coords):
    plt.plot(x_coords + (x_coords[0],), y_coords + (y_coords[0],), 'b-')
    plt.fill(x_coords, y_coords, 'r', alpha=0.5)
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    plot_isosceles_triangle()