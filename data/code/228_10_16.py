import matplotlib.pyplot as plt
vertices = [(0, 0), (4, 0), (2, 3)]
fill_color = 'blue'
alpha_value = 0.5

def plot_isosceles_triangle():
    x_coords, y_coords = zip(*vertices)
    plt.plot(x_coords + (x_coords[0],), y_coords + (y_coords[0],), 'b-')
    plt.fill(x_coords, y_coords, fill_color, alpha=alpha_value)
    plt.axis('equal')
    plt.show()
if __name__ == '__main__':
    plot_isosceles_triangle()