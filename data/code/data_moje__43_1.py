import math

def compute_pyramid_areas(base_edge, perpendicular_height):
    base_area = base_edge ** 2
    slant_height = math.sqrt((base_edge / 2) ** 2 + perpendicular_height ** 2)
    lateral_area = 0.5 * (4 * base_edge) * slant_height
    total_area = base_area + lateral_area
    return {"lateral_area": lateral_area, "total_area": total_area}

if __name__ == '__main__':
    base_edge = 4
    perpendicular_height = 6
    result = compute_pyramid_areas(base_edge, perpendicular_height)
    print(result)