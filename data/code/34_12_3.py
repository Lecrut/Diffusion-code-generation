import math

def calculate_cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * radius * radius
    return lateral_area + base_area

if __name__ == '__main__':
    sample_radius = 3.0
    sample_height = 5.0
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)