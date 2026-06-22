import math

def compute_square_pyramid_surface_area(base_edge, perpendicular_height):
    lateral_area = base_edge * perpendicular_height
    total_area = base_edge ** 2 + lateral_area
    return {"lateral_area": lateral_area, "total_area": total_area}

if __name__ == '__main__':
    base_edge = 5
    perpendicular_height = 12
    result = compute_square_pyramid_surface_area(base_edge, perpendicular_height)
    print(result)