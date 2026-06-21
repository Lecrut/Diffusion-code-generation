from typing import Union
HALF = 0.5

def triangle_area(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError('Base and height must be positive numbers')
    return HALF * base * height
if __name__ == '__main__':
    sample_base = 8.0
    sample_height = 3.0
    try:
        area_result = triangle_area(sample_base, sample_height)
        print(area_result)
    except ValueError as e:
        print(e)