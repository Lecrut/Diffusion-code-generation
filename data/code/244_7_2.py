def kite_area(d1, d2):
    return 0.5 * d1 * d2

def circle_area(radius):
    import math
    return math.pi * radius ** 2

if __name__ == '__main__':
    kite_d1 = 4
    kite_d2 = 6
    circle_radius = 5 / 2
    
    total_area = kite_area(kite_d1, kite_d2) + circle_area(circle_radius)
    print(total_area)