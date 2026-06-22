import math

def surface_area_of_square_pyramid(base_length: float, lateral_edge: float) -> float:
    if base_length <= 0 or lateral_edge <= 0:
        raise ValueError("Base length and lateral edge must be positive.")
    
    half_base = base_length / 2.0
    
    if lateral_edge < half_base:
        raise ValueError("Lateral edge must be at least half the base length for a valid square pyramid.")
    
    slant_height = math.sqrt(lateral_edge ** 2 - half_base ** 2)
    
    base_area = base_length ** 2
    triangular_face_area = (base_length * slant_height) / 2.0
    
    total_area = base_area + (4 * triangular_face_area)
    
    return total_area

if __name__ == '__main__':
    result = surface_area_of_square_pyramid(base_length=10.0, lateral_edge=13.0)
    print(result)