from typing import Union

def calculate_triangle_area(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        sample_base = 15.0
        sample_height = 8.0
        area_result = calculate_triangle_area(sample_base, sample_height)
        print(area_result)
    except ValueError as e:
        print(e)