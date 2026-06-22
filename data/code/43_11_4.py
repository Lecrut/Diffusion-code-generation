import math

def surface_area_square_pyramid(base_edge, height):
    half_base = base_edge / 2.0
    slant_height = math.sqrt(half_base ** 2 + height ** 2)
    base_area = base_edge ** 2
    lateral_area = 2 * base_edge * slant_height
    total_area = base_area + lateral_area
    return total_area

if __name__ == '__main__':
    base_edge = 10.0
    height = 12.0
    result = surface_area_square_pyramid(base_edge, height)
    print(result)