import math

def calculate_cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative.")
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * (radius ** 2)
    return lateral_area + base_area

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    surface_area = calculate_cylinder_surface_area(radius, height)
    print(surface_area)