from typing import Union

def calculate_area_square(side_length: float) -> float:
    if side_length < 0:
        raise ValueError('Side length cannot be negative')
    return side_length * side_length

def calculate_area_rectangle(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError('Length and width cannot be negative')
    return length * width

def calculate_area_circle(radius: float) -> float:
    import math
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return math.pi * radius * radius

if __name__ == '__main__':
    square_side = 5.0
    rectangle_length = 4.0
    rectangle_width = 6.0
    circle_radius = 3.0
    
    print("Area of Square:", calculate_area_square(square_side))
    print("Area of Rectangle:", calculate_area_rectangle(rectangle_length, rectangle_width))
    print(f"Area of Circle: {calculate_area_circle(circle_radius):.2f}")