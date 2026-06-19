from typing import Tuple

def calculate_triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == '__main__':
    triangle_dimensions: Tuple[float, float] = (7.0, 3.0)
    base_length, height_length = triangle_dimensions
    area_result = calculate_triangle_area(base_length, height_length)
    print(area_result)