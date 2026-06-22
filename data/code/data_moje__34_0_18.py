import math

def cylinder_total_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    base_area = math.pi * (radius ** 2)
    lateral_area = 2 * math.pi * radius * height
    return 2 * base_area + lateral_area

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    result = cylinder_total_surface_area(radius, height)
    print(result)