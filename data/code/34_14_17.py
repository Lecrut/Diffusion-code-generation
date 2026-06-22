import math

def cylinder_surface_area():
    radius = 5.0
    height = 10.0
    area = 2 * math.pi * radius * (radius + height)
    return area

if __name__ == '__main__':
    print(cylinder_surface_area())