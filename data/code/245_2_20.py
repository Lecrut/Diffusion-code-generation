import numpy as np

def triangles_have_equal_area(triangle1, triangle2):

    def calculate_area(triangle):
        x = np.array([p[0] for p in triangle])
        y = np.array([p[1] for p in triangle])
        return 0.5 * abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    area1 = calculate_area(triangle1)
    area2 = calculate_area(triangle2)
    return np.isclose(area1, area2)
if __name__ == '__main__':
    triangle1 = ((0, 0), (4, 0), (2, 3))
    triangle2 = ((-2, -3), (2, -3), (0, 0))
    print(triangles_have_equal_area(triangle1, triangle2))