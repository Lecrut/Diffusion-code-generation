import math

def calculate_cylinder_surface_area(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive numbers")
    base_area = math.pi * radius ** 2
    lateral_area = 2 * math.pi * radius * height
    return 2 * base_area + lateral_area

if __name__ == '__main__':
    test_radius = 5.0
    test_height = 10.0
    result = calculate_cylinder_surface_area(test_radius, test_height)
    print(result)