import math

def validate_ellipse_and_rectangle(ellipse_params, rectangle_params):
    if len(ellipse_params) != 2 or len(rectangle_params) != 2:
        raise ValueError("Both ellipse and rectangle parameters must be a list or tuple of two elements.")
    semi_major_axis, semi_minor_axis = ellipse_params
    side_length = rectangle_params[0]
    if semi_major_axis <= 0 or semi_minor_axis <= 0 or side_length <= 0:
        raise ValueError("All dimensions must be positive numbers.")

def calculate_area(ellipse_params):
    semi_major_axis, semi_minor_axis = ellipse_params
    return math.pi * semi_major_axis * semi_minor_axis

def calculate_area_difference(ellipse_params, rectangle_params):
    validate_ellipse_and_rectangle(ellipse_params, rectangle_params)
    ellipse_area = calculate_area(ellipse_params)
    side_length = rectangle_params[0]
    square_area = side_length ** 2
    difference = abs(ellipse_area - square_area)
    return difference

if __name__ == '__main__':
    ellipse_data = [5, 10]
    rectangle_data = [4, 10]
    result = calculate_area_difference(ellipse_data, rectangle_data)
    print(f"The difference between the areas is: {result}")