import math

def cylinder_surface_area(radius: float, height: float) -> float:
    if radius < 0 or height < 0:
        raise ValueError('Radius and height must be non-negative')
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * radius * radius
    return lateral_area + base_area
if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    area = cylinder_surface_area(radius, height)
    print(area)