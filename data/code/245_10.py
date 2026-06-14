import math
def calculate_circle_area(radius):
    return math.pi * radius**2
def calculate_rectangle_area(length, width):
    return length * width
if __name__ == '__main__':
    circle_radius = 5.0
    rectangle_length = 10.0
    rectangle_width = 5.0
    epsilon = 1e-9
    circle_area = calculate_circle_area(circle_radius)
    rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
    if abs(circle_area - rectangle_area) < epsilon:
        print("The areas are equal.")
    else:
        print("The areas are not equal.")