import math

def square_pyramid_surface_area(base_side_length: float, slant_height: float) -> float:
    base_area = base_side_length ** 2
    lateral_area = 2 * base_side_length * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side = 10.0
    slant = 12.0
    area = square_pyramid_surface_area(side, slant)
    print(area)