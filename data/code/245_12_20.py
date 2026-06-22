import math
EVALUATION_EPSILON = 1e-09

def area_ellipse(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def area_rectangle(width, height):
    return width * height

def check_area_equality(ellipse_semi_major_axis=5, ellipse_semi_minor_axis=3, rectangle_width=10, rectangle_height=6):
    ellipse_area = area_ellipse(ellipse_semi_major_axis, ellipse_semi_minor_axis)
    rectangle_area = area_rectangle(rectangle_width, rectangle_height)
    return math.isclose(ellipse_area, rectangle_area, rel_tol=EVALUATION_EPSILON)
if __name__ == '__main__':
    result = check_area_equality()
    print(result)