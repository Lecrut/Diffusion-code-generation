import math

def compute_ellipse_area(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    a = 5
    b = 3
    area = compute_ellipse_area(a, b)
    print(area)