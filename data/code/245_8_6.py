import math
def check_areas(radius, side):
    circle_area = math.pi * radius**2
    square_area = side**2
    epsilon = 1e-9
    return abs(circle_area - square_area) < epsilon
if __name__ == '__main__':
    r1 = 1.0
    s1 = math.pi
    print(check_areas(r1, s1))
    r2 = 3.0
    s2 = 3.0 * math.pi / 2.0
    print(check_areas(r2, s2))
    r3 = 5.0
    s3 = 7.0
    print(check_areas(r3, s3))