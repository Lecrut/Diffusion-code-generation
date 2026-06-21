from typing import Union

def calculate_area(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 12.0
    sample_height = 7.0
    try:
        area_result = calculate_area(sample_base, sample_height)
        print(area_result)
    except ValueError as e:
        print(e)