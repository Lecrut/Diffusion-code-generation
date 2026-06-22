import math

def compute_ellipse_area(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    sample_major = 10.5
    sample_minor = 7.2
    area = compute_ellipse_area(sample_major, sample_minor)
    print(area)