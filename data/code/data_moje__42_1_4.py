import math

def compute_ellipse_area(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    major = 10.5
    minor = 4.2
    area = compute_ellipse_area(major, minor)
    print(area)