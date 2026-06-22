from typing import Union

def calculate_area(length: float, width: float) -> float:
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

if __name__ == '__main__':
    try:
        length = 12.5
        width = 7.3
        area = calculate_area(length, width)
        print(f"Area of rectangle (L={length}, W={width}): {area}")
    except ValueError as e:
        print(e)