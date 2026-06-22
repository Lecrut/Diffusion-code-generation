import math

def calculate_cylinder_surface_area(radius: float, height: float) -> float:
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    result = calculate_cylinder_surface_area(5.0, 10.0)
    print(result)