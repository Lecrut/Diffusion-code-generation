import math

def calculate_cylinder_surface_area(radius, height):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * radius ** 2
    total_area = lateral_area + base_area
    return total_area

if __name__ == '__main__':
    sample_radius = 3.0
    sample_height = 5.0
    result = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(result)