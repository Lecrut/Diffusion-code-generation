from typing import Tuple

def calculate_triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height if base > 0 and height > 0 else 0.0

if __name__ == '__main__':
    dimensions: Tuple[float, float] = (18.0, 7.0)
    area = calculate_triangle_area(*dimensions)
    print(area)