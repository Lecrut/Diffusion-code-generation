import math

def calculate_ellipse_area(major_axis, minor_axis):
    if major_axis <= 0 or minor_axis <= 0:
        raise ValueError("Axis lengths must be positive numbers")
    a = major_axis / 2
    b = minor_axis / 2
    return math.pi * a * b

if __name__ == '__main__':
    sample_major = 10
    sample_minor = 6
    result = calculate_ellipse_area(sample_major, sample_minor)
    print(result)