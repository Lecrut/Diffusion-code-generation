import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return math.pi * radius**2

def calculate_rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return length * width

def shapes_equal_area(circle_radius, rectangle_length, rectangle_width):
    circle_area = calculate_circle_area(circle_radius)
    rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
    epsilon = 1e-9
    return abs(circle_area - rectangle_area) < epsilon

if __name__ == '__main__':
    try:
        circle_radius = 5.0
        rectangle_length = 10.0
        rectangle_width = 5.0
        if shapes_equal_area(circle_radius, rectangle_length, rectangle_width):
            print("The areas are equal.")
        else:
            print("The areas are not equal.")
    except ValueError as e:
        print(e)