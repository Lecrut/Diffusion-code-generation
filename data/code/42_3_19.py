import math

def ellipse_area(major_axis: float, minor_axis: float) -> float:
    if major_axis < 0 or minor_axis < 0:
        raise ValueError('Axis lengths must be non-negative.')
    semi_major = major_axis / 2.0
    semi_minor = minor_axis / 2.0
    return math.pi * semi_major * semi_minor
if __name__ == '__main__':
    major = 10.0
    minor = 6.0
    area = ellipse_area(major, minor)
    print(area)