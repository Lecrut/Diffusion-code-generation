def kite_area(d1, d2):
    return 0.5 * d1 * d2

def circle_area(radius):
    import math
    return math.pi * radius ** 2

def total_area():
    kite_d1 = 4
    kite_d2 = 6
    circle_radius = 5 / 2
    return kite_area(kite_d1, kite_d2) + circle_area(circle_radius)

if __name__ == '__main__':
    print(total_area())