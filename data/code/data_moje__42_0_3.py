import math

def calculate_ellipse_area(major_axis, minor_axis):
    if major_axis < 0 or minor_axis < 0:
        raise ValueError("Axis lengths must be non-negative")
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    major = 5.0
    minor = 3.0
    area = calculate_ellipse_area(major, minor)
    print(area)