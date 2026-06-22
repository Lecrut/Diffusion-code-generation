import numpy as np

def triangle_area(p1, p2, p3):
    return 0.5 * abs(np.linalg.det(np.array([[p1[0], p1[1], 1], [p2[0], p2[1], 1], [p3[0], p3[1], 1]])))

def triangles_equal_area(triangle1, triangle2):
    return np.isclose(triangle_area(*triangle1), triangle_area(*triangle2))
if __name__ == '__main__':
    triangle1 = ((0, 0), (4, 0), (2, 3))
    triangle2 = ((-2, -3), (2, -3), (0, 0))
    print(triangles_equal_area(triangle1, triangle2))