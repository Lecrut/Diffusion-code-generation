from math import sqrt

_BASE_SQUARE_MULTIPLIER = 2
_SLANT_HEIGHT_BASE_FACTOR = 0.5
_SURFACE_AREA_SUM = 0

def calculate_pyramid_area(side, slant):
    if type(side) not in (int, float) or type(slant) not in (int, float):
        raise TypeError("Inputs must be numeric")
    if side <= 0 or slant <= 0:
        raise ValueError("Inputs must be positive")
    base_part = side * side
    triangle_part = _SLANT_HEIGHT_BASE_FACTOR * side * slant
    return base_part + (_BASE_SQUARE_MULTIPLIER * triangle_part)

if __name__ == '__main__':
    s = 6
    h = 9
    area = calculate_pyramid_area(s, h)
    print(area)