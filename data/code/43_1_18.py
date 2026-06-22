import math

def compute_pyramid_areas(base_edge, perpendicular_height):
    base_area = base_edge ** 2
    slant_height = math.sqrt(perpendicular_height ** 2 + (base_edge / 2) ** 2)
    lateral_area = 0.5 * (4 * base_edge) * slant_height
    total_area = base_area + lateral_area
    return {
        "lateral_surface_area": lateral_area,
        "total_surface_area": total_area
    }

if __name__ == '__main__':
    hard_coded_base_edge = 5.0
    hard_coded_height = 12.0
    result = compute_pyramid_areas(hard_coded_base_edge, hard_coded_height)
    print(result)