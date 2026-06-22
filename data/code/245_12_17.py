import math

def area_ellipse(semi_major_axis, semi_minor_axis):
    if semi_major_axis <= 0 or semi_minor_axis <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive numbers")
    return math.pi * semi_major_axis * semi_minor_axis

def area_rectangle(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers")
    return width * height

def check_area_equality(semi_major_axis=5, semi_minor_axis=3, width=10, height=6):
    try:
        ellipse_area = area_ellipse(semi_major_axis, semi_minor_axis)
        rectangle_area = area_rectangle(width, height)
        return math.isclose(ellipse_area, rectangle_area)
    except ValueError as e:
        print(e)
        return None

if __name__ == '__main__':
    result = check_area_equality()
    if result is not None:
        print(result)