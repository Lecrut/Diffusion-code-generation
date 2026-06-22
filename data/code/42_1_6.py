import math

def compute_ellipse_area(major_axis, minor_axis):
    semi_major = major_axis / 2.0
    semi_minor = minor_axis / 2.0
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    major_axes = [10.0, 5.0, 2.0, 100.0]
    minor_axes = [6.0, 3.0, 1.5, 50.0]

    for ma, mi in zip(major_axes, minor_axes):
        area = compute_ellipse_area(ma, mi)
        print(area)