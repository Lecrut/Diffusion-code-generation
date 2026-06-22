from typing import Tuple

def calculate_areas(base: float, height: float, side_a: float, side_b: float) -> Tuple[float, float]:
    parallelogram_area = base * height
    trapezoid_area = 0.5 * (base + side_a) * height
    return parallelogram_area, trapezoid_area

if __name__ == '__main__':
    base = 10.0
    height = 5.0
    side_a = 8.0
    side_b = 6.0
    areas = calculate_areas(base, height, side_a, side_b)
    print(f"Parallelogram area: {areas[0]}")
    print(f"Trapezoid area: {areas[1]}")