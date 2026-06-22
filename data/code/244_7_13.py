import math

def kite_area(d1, d2):
    return 0.5 * d1 * d2

def circle_area(radius):
    return math.pi * radius ** 2

def validate_diagonals_and_radius(d1, d2, radius):
    if d1 <= 0 or d2 <= 0:
        raise ValueError("Diagonals must be positive")
    if radius <= 0:
        raise ValueError("Radius must be positive")

if __name__ == '__main__':
    kite_d1 = 4
    kite_d2 = 6
    circle_radius = 5 / 2
    
    validate_diagonals_and_radius(kite_d1, kite_d2, circle_radius)
    
    total_area = kite_area(kite_d1, kite_d2) + circle_area(circle_radius)
    print(total_area)