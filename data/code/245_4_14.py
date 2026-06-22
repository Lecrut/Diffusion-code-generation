from typing import Tuple

def calculate_areas(base: float, height: float, side_a: float, side_b: float) -> Tuple[float, float]:
    area_parallelogram = base * height
    area_trapezoid = 0.5 * (base + side_a) * height
    return area_parallelogram, area_trapezoid

if __name__ == '__main__':
    base = 10.0
    height = 5.0
    side_a = 7.0
    side_b = 9.0
    parallelogram_area, trapezoid_area = calculate_areas(base, height, side_a, side_b)
    print(f"Parallelogram area: {parallelogram_area}")
    print(f"Trapezoid area: {trapezoid_area}")