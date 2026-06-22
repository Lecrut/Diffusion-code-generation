from typing import Tuple

def calculate_areas(base_par: float, height_par: float, side_par: float, base_trap: float, height_trap: float) -> Tuple[float, float]:
    area_par = base_par * height_par
    area_trap = 0.5 * (base_par + base_trap) * height_trap
    return area_par, area_trap

if __name__ == '__main__':
    base_par = 10.0
    height_par = 5.0
    side_par = 7.0
    base_trap = 8.0
    height_trap = 6.0
    
    area_par, area_trap = calculate_areas(base_par, height_par, side_par, base_trap, height_trap)
    
    print(f"Area of Parallelogram: {area_par}")
    print(f"Area of Trapezoid: {area_trap}")