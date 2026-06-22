import matplotlib.pyplot as plt

def plot_isosceles_triangle(vertices):
    if len(vertices) != 3:
        raise ValueError("Vertices must consist of exactly three points.")
    
    for vertex in vertices:
        if not isinstance(vertex, tuple) or len(vertex) != 2:
            raise ValueError("Each vertex must be a tuple of two coordinates.")

    x_coords, y_coords = zip(*vertices)
    plt.plot(x_coords + (x_coords[0],), y_coords + (y_coords[0],), 'b-')
    plt.fill(x_coords, y_coords, 'r', alpha=0.5)
    plt.axis('equal')
    plt.title('Isosceles Triangle')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    vertices = [(0, 0), (4, 0), (2, 3)]
    plot_isosceles_triangle(vertices)