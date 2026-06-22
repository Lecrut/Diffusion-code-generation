import math

def calculate_total_surface_area(base_side: float, slant_height: float) -> float:
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area
if __name__ == '__main__':
    base_side = 10.0
    slant_height = 12.0
    result = calculate_total_surface_area(base_side, slant_height)
    print(result)