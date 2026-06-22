import matplotlib.pyplot as plt

def plot_isosceles_triangle():
    vertices = [(0, 0), (4, 0), (2, 3)]
    x_coords, y_coords = zip(*vertices)
    plt.plot(x_coords, y_coords, 'b-')
    plt.fill(x_coords, y_coords, 'b', alpha=0.5)
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    plot_isosceles_triangle()