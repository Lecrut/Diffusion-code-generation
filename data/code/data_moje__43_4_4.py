import math

def total_surface_area(base_side: float, slant_height: float) -> float:
    base_area = base_side ** 2
    lateral_area = 4 * (0.5 * base_side * slant_height)
    return base_area + lateral_area

if __name__ == '__main__':
    base = 10.0
    slant = 12.0
    result = total_surface_area(base, slant)
    print(result)