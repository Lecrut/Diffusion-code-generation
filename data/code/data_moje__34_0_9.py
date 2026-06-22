import math

def calculate_cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    sample_radius = 5
    sample_height = 10
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)