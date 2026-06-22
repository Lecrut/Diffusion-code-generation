import math

def calculate_cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError('Radius and height must be non-negative.')
    base_area = math.pi * radius ** 2
    lateral_area = 2 * math.pi * radius * height
    total_surface_area = 2 * base_area + lateral_area
    return total_surface_area
if __name__ == '__main__':
    RADIUS = 5.0
    HEIGHT = 10.0
    surface_area = calculate_cylinder_surface_area(RADIUS, HEIGHT)
    print(surface_area)