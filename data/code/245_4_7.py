from typing import Tuple

def calculate_areas(base_par: float, height_par: float, side_trapez: float, base1_trapez: float, base2_trapez: float) -> Tuple[float, float]:
    area_par = base_par * height_par
    area_trapez = 0.5 * (base1_trapez + base2_trapez) * side_trapez
    return area_par, area_trapez

if __name__ == '__main__':
    base_par = 10.0
    height_par = 5.0
    side_trapez = 8.0
    base1_trapez = 6.0
    base2_trapez = 4.0
    
    area_par, area_trapez = calculate_areas(base_par, height_par, side_trapez, base1_trapez, base2_trapez)
    
    print(f"Area of Parallelogram: {area_par}")
    print(f"Area of Trapezoid: {area_trapez}")