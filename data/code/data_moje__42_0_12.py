import math

def calculate_ellipse_area(major_axis, minor_axis):
    if major_axis <= 0 or minor_axis <= 0:
        raise ValueError("Axis lengths must be positive numbers.")
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    major = 10
    minor = 5
    area = calculate_ellipse_area(major, minor)
    print(area)