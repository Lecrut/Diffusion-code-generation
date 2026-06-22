import math

def calculate_ellipse_area(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    sample_major = 10
    sample_minor = 5
    area = calculate_ellipse_area(sample_major, sample_minor)
    print(area)