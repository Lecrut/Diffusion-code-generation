import math

def calculate_square_pyramid_surface_area(base_edge, height):
    half_base = base_edge / 2
    slant_height = math.sqrt(height ** 2 + half_base ** 2)
    base_area = base_edge ** 2
    lateral_area = 2 * base_edge * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base_edge_value = 10.0
    height_value = 12.0
    result = calculate_square_pyramid_surface_area(base_edge_value, height_value)
    print(result)