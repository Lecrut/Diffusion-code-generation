import math

def square_pyramid_surface_area(base_length, lateral_edge_length):
    if base_length <= 0 or lateral_edge_length <= 0:
        raise ValueError("Base length and lateral edge length must be positive")
    
    side_apothem = math.sqrt(lateral_edge_length ** 2 - (base_length / 2) ** 2)
    
    if side_apothem <= 0:
        raise ValueError("Invalid dimensions: lateral edge too short to form a pyramid")
    
    base_area = base_length ** 2
    lateral_area = 4 * (0.5 * base_length * side_apothem)
    
    return base_area + lateral_area

if __name__ == '__main__':
    base_len = 4
    lat_edge = 5
    result = square_pyramid_surface_area(base_len, lat_edge)
    print(result)