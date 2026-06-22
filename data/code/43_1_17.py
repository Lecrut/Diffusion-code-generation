import math

def compute_pyramid_areas(base_edge, height):
    half_base = base_edge / 2.0
    slant_height = math.sqrt(height**2 + half_base**2)
    base_area = base_edge ** 2
    lateral_area = base_edge * math.sqrt((base_edge**2)/4.0 + height**2)
    total_area = base_area + lateral_area
    return {"lateral_area": lateral_area, "total_area": total_area}

if __name__ == '__main__':
    base_edge = 10.0
    height = 12.0
    result = compute_pyramid_areas(base_edge, height)
    print(result)