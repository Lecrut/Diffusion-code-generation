def cylinder_surface_area():
    import math
    radius = 3.0
    height = 5.0
    area = 2 * math.pi * radius * (radius + height)
    return area

if __name__ == '__main__':
    result = cylinder_surface_area()
    print(result)