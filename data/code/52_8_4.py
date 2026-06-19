from typing import Union

def calculate_square_area(side_length: float) -> float:
    return side_length * side_length

def calculate_rectangle_area(length: float, width: float) -> float:
    return length * width

def calculate_circle_area(radius: float) -> float:
    import math
    return math.pi * radius * radius

def calculate_triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == '__main__':
    square_area = calculate_square_area(4.0)
    rectangle_area = calculate_rectangle_area(5.0, 3.0)
    circle_area = calculate_circle_area(2.0)
    triangle_area = calculate_triangle_area(6.0, 4.0)

    print(f"Square Area: {square_area}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area:.2f}")
    print(f"Triangle Area: {triangle_area}")