import math

def cylinder_surface_area(radius: float, height: float) -> float:
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * (radius ** 2)
    return lateral_area + base_area

if __name__ == '__main__':
    RADIUS = 3.0
    HEIGHT = 5.0
    result = cylinder_surface_area(RADIUS, HEIGHT)
    print(result)