import math

def compute_pyramid_areas(base_edge, perpendicular_height):
    if base_edge <= 0 or perpendicular_height <= 0:
        raise ValueError("Base edge and height must be positive")
    
    half_base = base_edge / 2.0
    
    slant_height = math.sqrt(half_base ** 2 + perpendicular_height ** 2)
    
    lateral_area = base_edge * math.sqrt((base_edge / 2.0) ** 2 + perpendicular_height ** 2)
    
    base_area = base_edge ** 2
    
    total_area = lateral_area + base_area
    
    return {
        "lateral_area": lateral_area,
        "total_area": total_area
    }

if __name__ == '__main__':
    base_edge = 10.0
    perpendicular_height = 12.0
    
    result = compute_pyramid_areas(base_edge, perpendicular_height)
    
    print(result)