import math

def calculate_square_pyramid_surface_area(base_length, lateral_edge_length):
    if base_length <= 0 or lateral_edge_length <= 0:
        raise ValueError("Base length and lateral edge length must be positive.")
    half_base = base_length / 2
    if lateral_edge_length <= half_base:
        raise ValueError("Lateral edge length must be greater than half the base length.")
    slant_height = math.sqrt(lateral_edge_length ** 2 - half_base ** 2)
    base_area = base_length ** 2
    lateral_area = 2 * base_length * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_len = 6.0
    lateral_edge_len = 5.0
    result = calculate_square_pyramid_surface_area(base_len, lateral_edge_len)
    print(result)