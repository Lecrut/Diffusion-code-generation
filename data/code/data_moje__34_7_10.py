import math

def cylinder_surface_area(radius: float, height: float) -> float:
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    radius_value = 5
    height_value = 10
    result = cylinder_surface_area(radius_value, height_value)
    print(result)