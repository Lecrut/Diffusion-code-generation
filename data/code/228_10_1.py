import matplotlib.pyplot as plt

def plot_isosceles_triangle():
    x = [0, 4, 2, 0]
    y = [0, 0, 3, 0]
    plt.plot(x, y)
    plt.fill(x, y, 'blue', alpha=0.5)
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    plot_isosceles_triangle()