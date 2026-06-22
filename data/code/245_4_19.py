from typing import Tuple

def calculate_areas(base_parallelogram: float, height_parallelogram: float, base_trapezoid: float, height_trapezoid: float, side_a: float, side_b: float) -> Tuple[float, float]:
    area_parallelogram = base_parallelogram * height_parallelogram
    area_trapezoid = 0.5 * (base_trapezoid + side_a + side_b) * height_trapezoid
    return area_parallelogram, area_trapezoid

if __name__ == '__main__':
    base_parallelogram = 10.0
    height_parallelogram = 5.0
    base_trapezoid = 8.0
    height_trapezoid = 6.0
    side_a = 7.0
    side_b = 9.0
    
    area_parallelogram, area_trapezoid = calculate_areas(base_parallelogram, height_parallelogram, base_trapezoid, height_trapezoid, side_a, side_b)
    
    print(f"Area of Parallelogram: {area_parallelogram}")
    print(f"Area of Trapezoid: {area_trapezoid}")