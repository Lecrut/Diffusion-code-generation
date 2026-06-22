import math

def compute_ellipse_area(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    semi_major = 5
    semi_minor = 3
    area = compute_ellipse_area(semi_major, semi_minor)
    print(area)