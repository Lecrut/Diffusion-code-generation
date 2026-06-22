import math

def surface_area_square_pyramid(base_side: float, slant_height: float) -> float:
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_side = 4.0
    slant_height = 5.0
    result = surface_area_square_pyramid(base_side, slant_height)
    print(result)