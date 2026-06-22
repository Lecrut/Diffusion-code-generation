KITE_AREA_CONSTANT = 0.5

def kite_area(diagonal1, diagonal2):
    return KITE_AREA_CONSTANT * diagonal1 * diagonal2

import math

CIRCLE_AREA_MULTIPLIER = math.pi

def circle_area(diameter):
    radius = diameter / 2
    return CIRCLE_AREA_MULTIPLIER * radius ** 2

if __name__ == '__main__':
    kite_d1 = 4
    kite_d2 = 6
    circle_diameter = 5
    total_area = kite_area(kite_d1, kite_d2) + circle_area(circle_diameter)
    print(total_area)