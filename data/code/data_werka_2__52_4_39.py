from typing import Union

def calculate_circle_area(radius: float) -> float:
    return 3.14159 * radius ** 2

def calculate_square_area(side_length: float) -> float:
    return side_length ** 2

def calculate_rectangle_area(length: float, width: float) -> float:
    return length * width

def calculate_triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == '__main__':
    circle_area = calculate_circle_area(5.0)
    square_area = calculate_square_area(4.0)
    rectangle_area = calculate_rectangle_area(6.0, 3.0)
    triangle_area = calculate_triangle_area(7.0, 2.0)

    print(f"Circle Area: {circle_area}")
    print(f"Square Area: {square_area}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Triangle Area: {triangle_area}")