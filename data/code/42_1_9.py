import math

def compute_ellipse_area(major_axis, minor_axis):
    semi_major = major_axis / 2.0
    semi_minor = minor_axis / 2.0
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    sample_major = 10.0
    sample_minor = 6.0
    result = compute_ellipse_area(sample_major, sample_minor)
    print(result)