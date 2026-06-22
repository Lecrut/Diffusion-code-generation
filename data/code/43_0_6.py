import math

def square_pyramid_surface_area(base_side: float, slant_height: float) -> float:
    base_area = base_side * base_side
    lateral_area = 2 * base_side * slant_height
    total_area = base_area + lateral_area
    return total_area

if __name__ == '__main__':
    side = 10.0
    slant = 12.0
    area = square_pyramid_surface_area(side, slant)
    print(area)