from typing import Union

def calculate_area_square(side_length: float) -> float:
    return side_length * side_length

def calculate_area_rectangle(length: float, width: float) -> float:
    return length * width

def calculate_area_circle(radius: float) -> float:
    import math
    return math.pi * radius * radius

if __name__ == '__main__':
    square_side = 5.0
    rectangle_length = 4.0
    rectangle_width = 6.0
    circle_radius = 3.0

    print("Area of Square:", calculate_area_square(square_side))
    print("Area of Rectangle:", calculate_area_rectangle(rectangle_length, rectangle_width))
    print("Area of Circle:", calculate_area_circle(circle_radius))