import math

LATERAL_FACTOR = 2
BASE_MULTIPLIER = 2

def compute_cylinder_surface_area(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive values")
    lateral_area = LATERAL_FACTOR * math.pi * radius * height
    base_area = BASE_MULTIPLIER * math.pi * (radius * radius)
    return lateral_area + base_area

if __name__ == '__main__':
    sample_radius = 7.5
    sample_height = 12.0
    area_result = compute_cylinder_surface_area(sample_radius, sample_height)
    print(area_result)