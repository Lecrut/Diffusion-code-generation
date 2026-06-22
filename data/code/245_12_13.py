import math

def area_ellipse(semi_major_axis, semi_minor_axis):
    if semi_major_axis <= 0 or semi_minor_axis <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive.")
    return math.pi * semi_major_axis * semi_minor_axis

def area_rectangle(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive.")
    return width * height

def check_area_equality(semi_major_axis=5, semi_minor_axis=3, width=10, height=6):
    ellipse_area = area_ellipse(semi_major_axis, semi_minor_axis)
    rectangle_area = area_rectangle(width, height)
    return math.isclose(ellipse_area, rectangle_area)

if __name__ == '__main__':
    try:
        result = check_area_equality()
        print(result)
    except ValueError as e:
        print(e)