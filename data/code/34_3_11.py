import math

def calculate_cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    r = 3.0
    h = 5.0
    result = calculate_cylinder_surface_area(r, h)
    print(result)