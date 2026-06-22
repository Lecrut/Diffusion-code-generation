import math

def calculate_cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative.")
    return 2 * math.pi * radius * (radius + height)

if __name__ == "__main__":
    radius = 5.0
    height = 10.0
    result = calculate_cylinder_surface_area(radius, height)
    print(result)