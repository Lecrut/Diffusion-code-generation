import math

def cylinder_total_surface_area(radius, height):
    area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
    return area

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    result = cylinder_total_surface_area(radius, height)
    print(result)