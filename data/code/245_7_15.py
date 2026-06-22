import math

def calculate_ellipse_area(semi_major_axis, semi_minor_axis):
    if semi_major_axis <= 0 or semi_minor_axis <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive numbers.")
    return math.pi * semi_major_axis * semi_minor_axis

def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

def compare_areas(ellipse_params, rectangle_params):
    ellipse_area = calculate_ellipse_area(*ellipse_params)
    rectangle_area = calculate_rectangle_area(*rectangle_params)
    area_difference = abs(ellipse_area - rectangle_area)
    if area_difference == 0:
        print("The areas are equal.")
    else:
        print(f"The difference between the areas is: {area_difference}")
    return area_difference

if __name__ == '__main__':
    ellipse_data = (5, 10)
    rectangle_data = (4, 10)
    compare_areas(ellipse_data, rectangle_data)