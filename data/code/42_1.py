import math

def compute_ellipse_area(major_axis, minor_axis):
    if major_axis <= 0 or minor_axis <= 0:
        raise ValueError("Axis dimensions must be positive")
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    major = 10.5
    minor = 7.2
    area = compute_ellipse_area(major, minor)
    print(area)