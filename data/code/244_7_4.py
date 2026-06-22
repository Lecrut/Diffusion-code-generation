def kite_area(d1, d2):
    return 0.5 * d1 * d2

def circle_area(radius):
    import math
    return math.pi * radius ** 2

def total_area(kite_d1, kite_d2, circle_diameter):
    kite_radius = kite_d1 / (2 * math.sin(math.radians(90)))
    circle_radius = circle_diameter / 2
    return kite_area(kite_d1, kite_d2) + circle_area(circle_radius)

if __name__ == '__main__':
    print(total_area(4, 6, 5))