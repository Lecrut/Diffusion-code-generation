from typing import Union

def validate_dimensions(base: float, height: float) -> None:
    if base <= 0:
        raise ValueError("Base must be a positive number")
    if height <= 0:
        raise ValueError("Height must be a positive number")

def triangle_area(base: float, height: float) -> float:
    validate_dimensions(base, height)
    return 0.5 * base * height

if __name__ == '__main__':
    test_base = 8.0
    test_height = 3.0
    try:
        result_area = triangle_area(test_base, test_height)
        print(result_area)
    except ValueError as e:
        print(e)