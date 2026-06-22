import math

def square_pyramid_surface_area(base_side: float, slant_height: float) -> float:
    base_area = base_side * base_side
    triangular_area = (base_side * slant_height) / 2.0
    total_area = base_area + (4 * triangular_area)
    return total_area

if __name__ == '__main__':
    side = 10.0
    height = 12.0
    result = square_pyramid_surface_area(side, height)
    print(result)