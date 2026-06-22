from typing import Tuple
HALF = 0.5

def calculate_triangle_area(base: float, height: float) -> float:
    return HALF * base * height
if __name__ == '__main__':
    sample_dimensions: Tuple[float, float] = (20.0, 7.0)
    area = calculate_triangle_area(*sample_dimensions)
    print(area)