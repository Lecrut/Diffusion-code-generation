from typing import Tuple

def triangle_area(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_values: Tuple[float, float] = (8.0, 6.0)
    try:
        area_result = triangle_area(*sample_values)
        print(area_result)
    except ValueError as e:
        print(e)