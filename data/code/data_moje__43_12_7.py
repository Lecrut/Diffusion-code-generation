import math

def surface_area_of_square_pyramid(base_length: float, lateral_edge: float) -> float:
    if base_length <= 0 or lateral_edge <= 0:
        raise ValueError("Dimensions must be positive")
    
    half_base = base_length / 2
    
    slant_height_squared = lateral_edge ** 2 - half_base ** 2
    
    if slant_height_squared < 0:
        raise ValueError("Lateral edge is too short for the given base")
    
    slant_height = math.sqrt(slant_height_squared)
    
    base_area = base_length ** 2
    
    triangular_face_area = (base_length * slant_height) / 2
    
    total_surface_area = base_area + 4 * triangular_face_area
    
    return total_surface_area

if __name__ == '__main__':
    result = surface_area_of_square_pyramid(4, 5)
    print(result)