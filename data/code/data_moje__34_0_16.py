import math

def calculate_cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * radius * radius
    return lateral_area + base_area

if __name__ == '__main__':
    test_radius = 5
    test_height = 10
    result = calculate_cylinder_surface_area(test_radius, test_height)
    print(result)