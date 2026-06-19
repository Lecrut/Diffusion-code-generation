from typing import Tuple

def calculate_triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == '__main__':
    triangle_dimensions: Tuple[float, float] = (7.0, 4.0)
    base_value, height_value = triangle_dimensions
    area_result = calculate_triangle_area(base_value, height_value)
    print(area_result)