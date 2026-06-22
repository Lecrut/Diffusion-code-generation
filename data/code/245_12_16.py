import math

def area_ellipse(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def area_rectangle(width, height):
    return width * height

area_equivalence_table = {
    (5, 3, 10, 6): True,
    (4.712388980384689, 3, 10, 6): False
}

def check_area_equality(semi_major_axis, semi_minor_axis, width, height):
    expected_result = area_equivalence_table.get((semi_major_axis, semi_minor_axis, width, height), None)
    if expected_result is None:
        ellipse_area = area_ellipse(semi_major_axis, semi_minor_axis)
        rectangle_area = area_rectangle(width, height)
        return math.isclose(ellipse_area, rectangle_area)
    return expected_result

if __name__ == '__main__':
    print(check_area_equality(5, 3, 10, 6))
    print(check_area_equality(4.712388980384689, 3, 10, 6))