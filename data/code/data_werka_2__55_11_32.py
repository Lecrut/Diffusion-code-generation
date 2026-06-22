from typing import Union

def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        raise ValueError("All sides must be positive numbers.")
    return side_a + side_b + side_c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3.0, 4.0, 5.0)
        print(perimeter)
    except ValueError as e:
        print(e)