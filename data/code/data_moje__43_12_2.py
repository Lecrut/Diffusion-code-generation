import math

def surface_area_square_pyramid(base_length, lateral_edge_length):
    if base_length <= 0 or lateral_edge_length <= 0:
        raise ValueError("Lengths must be positive")
    if base_length / 2 >= lateral_edge_length:
        raise ValueError("Lateral edge must be greater than half the base length to form a pyramid")
    half_base = base_length / 2
    slant_height = math.sqrt(lateral_edge_length**2 - half_base**2)
    base_area = base_length * base_length
    lateral_area = 4 * (0.5 * base_length * slant_height)
    return base_area + lateral_area

if __name__ == '__main__':
    base = 6.0
    edge = 5.0
    result = surface_area_square_pyramid(base, edge)
    print(result)