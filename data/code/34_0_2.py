import math

def calculate_cylinder_surface_area(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive numbers")
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * radius ** 2
    return lateral_area + base_area

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    area = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(area)