import math

def compute_cylinder_base_area(radius):
    return math.pi * radius ** 2

def compute_cylinder_lateral_area(radius, height):
    return 2 * math.pi * radius * height

def compute_cylinder_surface_area(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive values.")
    base_area = compute_cylinder_base_area(radius)
    lateral_area = compute_cylinder_lateral_area(radius, height)
    total_surface_area = 2 * base_area + lateral_area
    return total_surface_area

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    result = compute_cylinder_surface_area(sample_radius, sample_height)
    print(result)