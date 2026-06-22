import numpy as np

def polygon_area(points):
    x = points[:, 0]
    y = points[:, 1]
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

def circle_area(radius):
    return np.pi * radius ** 2

if __name__ == '__main__':
    polygon_points = np.array([(0,0), (2,0), (2,2), (0,2)])
    circle_radius = 1.5
    print("Polygon area:", polygon_area(polygon_points))
    print("Circle area:", circle_area(circle_radius))