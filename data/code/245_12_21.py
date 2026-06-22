import math

def area_ellipse(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def area_rectangle(width, height):
    return width * height

def check_area_equality(semi_major_axis, semi_minor_axis, width, height):
    ellipse_area = area_ellipse(semi_major_axis, semi_minor_axis)
    rectangle_area = area_rectangle(width, height)
    return math.isclose(ellipse_area, rectangle_area)

if __name__ == '__main__':
    sample_semi_major_axis = 5
    sample_semi_minor_axis = 3
    sample_width = 12
    sample_height = 4.712388980384689

    result = check_area_equality(sample_semi_major_axis, sample_semi_minor_axis, sample_width, sample_height)
    print(result)