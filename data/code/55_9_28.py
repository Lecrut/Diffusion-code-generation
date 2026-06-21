from typing import Union

def calculate_triangle_perimeter(side1: Union[int, float], side2: Union[int, float], side3: Union[int, float]) -> Union[int, float]:
    if any(side <= 0 for side in [side1, side2, side3]):
        raise ValueError("Side lengths must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)