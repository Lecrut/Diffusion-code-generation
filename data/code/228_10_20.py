import matplotlib.pyplot as plt
X0, Y0 = (0, 0)
X1, Y1 = (4, 0)
X2, Y2 = (2, 3)

def plot_isosceles_triangle():
    x_coords = [X0, X1, X2, X0]
    y_coords = [Y0, Y1, Y2, Y0]
    plt.plot(x_coords, y_coords, 'b-')
    plt.fill(x_coords, y_coords, 'blue', alpha=0.5)
    plt.axis('equal')
    plt.show()
if __name__ == '__main__':
    plot_isosceles_triangle()