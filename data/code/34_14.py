import math

def compute_cylinder_surface_area(radius: float, height: float) -> float:
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    _radius = 3
    _height = 5
    result = compute_cylinder_surface_area(_radius, _height)
    print(result)