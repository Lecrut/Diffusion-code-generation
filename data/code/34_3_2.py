import math

def cylinder_surface_area(radius: float, height: float) -> float:
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative.")
    return 2 * math.pi * radius * height + 2 * math.pi * (radius ** 2)

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    result = cylinder_surface_area(radius, height)
    print(result)