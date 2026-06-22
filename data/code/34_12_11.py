import math

def calculate_cylinder_surface_area(radius, height):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)