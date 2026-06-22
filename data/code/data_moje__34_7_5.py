import math

def calculate_cylinder_surface_area(radius: float, height: float) -> float:
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    area = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(area)