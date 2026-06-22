import math

def cylinder_surface_area(radius: float, height: float) -> float:
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * radius * radius
    total_area = lateral_area + base_area
    return total_area

if __name__ == '__main__':
    radius = 5
    height = 10
    result = cylinder_surface_area(radius, height)
    print(result)