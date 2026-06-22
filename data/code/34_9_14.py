import math

def cylinder_surface_area(radius, height):
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * (radius ** 2)
    total_area = lateral_area + base_area
    return total_area

if __name__ == '__main__':
    RADIUS = 5
    HEIGHT = 10
    result = cylinder_surface_area(RADIUS, HEIGHT)
    print(result)