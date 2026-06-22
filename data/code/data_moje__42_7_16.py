import math

def calculate_ellipse_area(semi_major_axis, semi_minor_axis):
    if not isinstance(semi_major_axis, (int, float)):
        raise TypeError("semi_major_axis must be a number")
    if not isinstance(semi_minor_axis, (int, float)):
        raise TypeError("semi_minor_axis must be a number")
    if semi_major_axis < 0:
        raise ValueError("semi_major_axis must be non-negative")
    if semi_minor_axis < 0:
        raise ValueError("semi_minor_axis must be non-negative")
    if math.isinf(semi_major_axis) or math.isinf(semi_minor_axis):
        raise ValueError("Axes must be finite")
    if math.isnan(semi_major_axis) or math.isnan(semi_minor_axis):
        raise ValueError("Axes must not be NaN")
    return math.pi * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    a = 5.0
    b = 3.0
    area = calculate_ellipse_area(a, b)
    print(area)