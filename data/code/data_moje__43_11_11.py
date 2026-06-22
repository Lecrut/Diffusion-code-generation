import math

def calculate_square_pyramid_surface_area(base_edge, height):
    half_base = base_edge / 2
    slant_height = math.sqrt(half_base**2 + height**2)
    base_area = base_edge**2
    lateral_area = 4 * (0.5 * base_edge * slant_height)
    total_area = base_area + lateral_area
    return total_area

if __name__ == '__main__':
    base_edge = 10.0
    height = 12.0
    result = calculate_square_pyramid_surface_area(base_edge, height)
    print(result)