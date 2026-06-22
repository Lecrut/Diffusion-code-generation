import math

def calculate_ellipse_area(major_axis, minor_axis):
    if major_axis <= 0 or minor_axis <= 0:
        raise ValueError("Axis values must be positive")
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    sample_major = 10.0
    sample_minor = 5.0
    result = calculate_ellipse_area(sample_major, sample_minor)
    print(result)