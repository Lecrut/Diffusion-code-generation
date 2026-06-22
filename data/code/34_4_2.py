def cylinder_surface_area():
    radius = 5.0
    height = 10.0
    import math
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    result = cylinder_surface_area()
    print(result)