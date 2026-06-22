from typing import Union

def calculate_triangle_area(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    return 0.5 * base * height

if __name__ == '__main__':
    test_base = 8.0
    test_height = 3.0
    try:
        result_area = calculate_triangle_area(test_base, test_height)
        print(result_area)
    except ValueError as e:
        print(e)