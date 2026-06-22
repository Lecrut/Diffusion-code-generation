import math

def calculate_cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    result = calculate_cylinder_surface_area(5, 10)
    print(result)