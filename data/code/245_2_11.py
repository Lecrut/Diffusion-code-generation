import numpy as np

def triangle_area(p1, p2, p3):
    return 0.5 * abs(np.linalg.det(np.array([[p1[0], p1[1], 1],
                                            [p2[0], p2[1], 1],
                                            [p3[0], p3[1], 1]])))

def triangles_equal_area(t1, t2):
    return np.isclose(triangle_area(*t1), triangle_area(*t2))

if __name__ == '__main__':
    print(triangles_equal_area(((0, 0), (4, 0), (2, 3)), ((-2, -3), (2, -3), (0, 0))))