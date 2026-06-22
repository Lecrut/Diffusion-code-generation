import math

def calculate_ellipse_area(semi_major_axis, semi_minor_axis):
    if not isinstance(semi_major_axis, (int, float)) or not isinstance(semi_minor_axis, (int, float)):
        raise TypeError("Semi-major and semi-minor axes must be numeric.")
    if semi_major_axis <= 0 or semi_minor_axis <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive numbers.")
    return math.pi * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    radius_x = 7.5
    radius_y = 4.2
    area_value = calculate_ellipse_area(radius_x, radius_y)
    print(area_value)