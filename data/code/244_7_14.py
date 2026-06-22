import math

def kite_area(d1, d2):
    return 0.5 * d1 * d2

def circle_area(radius):
    return math.pi * radius ** 2

def calculate_total_area(kite_d1, kite_d2, circle_radius):
    if not all(isinstance(i, (int, float)) for i in [kite_d1, kite_d2, circle_radius]):
        raise ValueError("All inputs must be numbers")
    return kite_area(kite_d1, kite_d2) + circle_area(circle_radius)

if __name__ == '__main__':
    kite_d1 = 4
    kite_d2 = 6
    circle_radius = 5 / 2
    try:
        total_area = calculate_total_area(kite_d1, kite_d2, circle_radius)
        print(total_area)
    except ValueError as e:
        print(e)