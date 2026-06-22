def calculate_square_pyramid_surface_area(base_length, lateral_edge_length):
    if base_length <= 0 or lateral_edge_length <= 0:
        raise ValueError("Lengths must be positive numbers")
    if lateral_edge_length * 2 <= base_length:
        raise ValueError("Lateral edge must be long enough to form a pyramid with the given base")
    import math
    base_area = base_length * base_length
    half_base = base_length / 2
    slant_height = math.sqrt(lateral_edge_length**2 - half_base**2)
    triangle_area = 0.5 * base_length * slant_height
    lateral_area = 4 * triangle_area
    total_surface_area = base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    base_len = 6.0
    lateral_edge_len = 5.0
    result = calculate_square_pyramid_surface_area(base_len, lateral_edge_len)
    print(result)