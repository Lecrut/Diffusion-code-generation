import math

def cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        return 0.0
    lateral_area = 2 * math.pi * radius * height
    base_area = math.pi * radius * radius
    total_area = lateral_area + 2 * base_area
    return total_area

if __name__ == '__main__':
    r = 5.0
    h = 10.0
    result = cylinder_surface_area(r, h)
    print(result)