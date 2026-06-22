import math

def get_semi_axis(full_axis):
    return full_axis / 2.0

def calculate_ellipse_area(major_axis, minor_axis):
    if major_axis < 0 or minor_axis < 0:
        raise ValueError("Axis lengths cannot be negative")
    semi_major = get_semi_axis(major_axis)
    semi_minor = get_semi_axis(minor_axis)
    area_value = math.pi * semi_major * semi_minor
    return area_value

if __name__ == '__main__':
    input_major = 20.0
    input_minor = 8.0
    final_area = calculate_ellipse_area(input_major, input_minor)
    print(final_area)