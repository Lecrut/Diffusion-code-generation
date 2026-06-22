import math

def compute_ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    major_axis = 10.0
    minor_axis = 5.0
    area = compute_ellipse_area(major_axis, minor_axis)
    print(area)