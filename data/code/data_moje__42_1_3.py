import math

def compute_ellipse_area(major_axis, minor_axis):
    radius_a = major_axis / 2.0
    radius_b = minor_axis / 2.0
    area = math.pi * radius_a * radius_b
    return area

if __name__ == '__main__':
    major = 10.0
    minor = 6.0
    result = compute_ellipse_area(major, minor)
    print(result)