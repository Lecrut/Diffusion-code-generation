import math

def calculate_ellipse_area(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    sample_major = 5.0
    sample_minor = 3.0
    area = calculate_ellipse_area(sample_major, sample_minor)
    print(area)