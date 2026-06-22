import numpy as np

def is_area_equal(triangle1, triangle2):
    x1, y1 = zip(*triangle1)
    x2, y2 = zip(*triangle2)
    area1 = 0.5 * abs(np.dot(x1, np.roll(y1, 1)) - np.dot(y1, np.roll(x1, 1)))
    area2 = 0.5 * abs(np.dot(x2, np.roll(y2, 1)) - np.dot(y2, np.roll(x2, 1)))
    return np.isclose(area1, area2)
if __name__ == '__main__':
    triangle1 = ((0, 0), (4, 0), (2, 3))
    triangle2 = ((-2, -3), (2, -3), (0, 0))
    print(is_area_equal(triangle1, triangle2))