import math

def calculate_area_difference(ellipse_params, rectangle_params):
    semi_major_axis, semi_minor_axis = ellipse_params
    side_length = rectangle_params[0]

    if semi_major_axis <= 0 or semi_minor_axis <= 0 or side_length <= 0:
        raise ValueError("All parameters must be positive numbers.")

    ellipse_area = math.pi * semi_major_axis * semi_minor_axis
    rectangle_area = side_length ** 2

    difference = abs(ellipse_area - rectangle_area)
    return difference

if __name__ == '__main__':
    ellipse_data = (3, 4)
    rectangle_data = (5,)
    result = calculate_area_difference(ellipse_data, rectangle_data)
    print(f"The difference between the areas is: {result}")