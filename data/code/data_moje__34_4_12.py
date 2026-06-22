def cylinder_surface_area(radius, height):
    pi = 3.141592653589793
    return 2 * pi * radius * (radius + height)

if __name__ == '__main__':
    r = 5
    h = 10
    print(cylinder_surface_area(r, h))