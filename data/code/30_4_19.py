import math

AREA_CONSTANT = 2

def get_circle_area(radius):
    diameter = radius * AREA_CONSTANT
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    r = 4
    computed_area = get_circle_area(r)
    print(computed_area)