from typing import Union

def calculate_area_square(side_length: float) -> float:
    return side_length * side_length

def calculate_area_rectangle(length: float, width: float) -> float:
    return length * width

def calculate_area_circle(radius: float) -> float:
    import math
    return math.pi * radius * radius

def calculate_area_triangle(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == '__main__':
    square_area = calculate_area_square(4.0)
    rectangle_area = calculate_area_rectangle(5.0, 3.0)
    circle_area = calculate_area_circle(2.0)
    triangle_area = calculate_area_triangle(6.0, 4.0)

    print(f"Square Area: {square_area}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area:.2f}")
    print(f"Triangle Area: {triangle_area}")