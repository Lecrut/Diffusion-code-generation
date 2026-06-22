import math

def surface_area_square_pyramid(base_side, slant_height):
    base_area = base_side * base_side
    triangle_area = 0.5 * base_side * slant_height
    total_lateral_area = 4 * triangle_area
    return base_area + total_lateral_area

if __name__ == '__main__':
    base = 10.0
    slant = 12.0
    result = surface_area_square_pyramid(base, slant)
    print(result)