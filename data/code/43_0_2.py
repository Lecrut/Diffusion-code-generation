import math

def square_pyramid_surface_area(base_side: float, slant_height: float) -> float:
    if base_side <= 0 or slant_height <= 0:
        raise ValueError('Base side and slant height must be positive.')
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area
if __name__ == '__main__':
    base = 10
    height = 12
    result = square_pyramid_surface_area(base, height)
    print(result)