import math

def area_ellipse(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def area_rectangle(width, height):
    return width * height

def check_area_equality(ellipse_semi_major_axis, ellipse_semi_minor_axis, rectangle_width, rectangle_height):
    ellipse_area = area_ellipse(ellipse_semi_major_axis, ellipse_semi_minor_axis)
    rectangle_area = area_rectangle(rectangle_width, rectangle_height)
    return math.isclose(ellipse_area, rectangle_area)
if __name__ == '__main__':
    print(check_area_equality(5, 3, 10, 4.712388980384689))