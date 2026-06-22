import numpy as np

def polygon_area(points):
    x = points[:, 0]
    y = points[:, 1]
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

if __name__ == '__main__':
    points = np.array([(0,0), (2,0), (2,2), (0,2)])
    area_polygon = polygon_area(points)
    radius_circle = 1.5
    area_circle = np.pi * radius_circle ** 2
    print(f"Area of the polygon: {area_polygon}")
    print(f"Area of the circle: {area_circle}")