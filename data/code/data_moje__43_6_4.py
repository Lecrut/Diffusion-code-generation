import math

def surface_area_square_pyramid(base_edge, slant_height):
    if base_edge <= 0 or slant_height <= 0:
        raise ValueError("Dimensions must be positive")
    base_area = base_edge ** 2
    lateral_area = 2 * base_edge * slant_height
    total_area = base_area + lateral_area
    return total_area

if __name__ == '__main__':
    base = 10
    slant = 13
    result = surface_area_square_pyramid(base, slant)
    print(result)