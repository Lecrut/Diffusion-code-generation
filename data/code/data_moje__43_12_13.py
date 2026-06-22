import math

def calculate_square_pyramid_surface_area(base_length, lateral_edge_length):
    if base_length <= 0 or lateral_edge_length <= 0:
        raise ValueError("Base length and lateral edge length must be positive")
    if lateral_edge_length <= (base_length / math.sqrt(2)):
        raise ValueError("Lateral edge length must be greater than half the base diagonal")
    
    base_area = base_length * base_length
    half_base = base_length / 2
    triangle_height = math.sqrt(lateral_edge_length**2 - half_base**2)
    triangular_face_area = 0.5 * base_length * triangle_height
    lateral_surface_area = 4 * triangular_face_area
    total_surface_area = base_area + lateral_surface_area
    return total_surface_area

if __name__ == '__main__':
    sample_base = 10.0
    sample_lateral_edge = 13.0
    result = calculate_square_pyramid_surface_area(sample_base, sample_lateral_edge)
    print(result)