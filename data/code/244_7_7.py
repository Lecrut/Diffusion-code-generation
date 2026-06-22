import math

def validate_diagonals(d1, d2):
    if not (isinstance(d1, (int, float)) and isinstance(d2, (int, float))):
        raise ValueError("Diagonals must be numbers")
    if d1 <= 0 or d2 <= 0:
        raise ValueError("Diagonals must be positive")

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number")
    if radius <= 0:
        raise ValueError("Radius must be positive")

def kite_area(d1, d2):
    validate_diagonals(d1, d2)
    return 0.5 * d1 * d2

def circle_area(radius):
    validate_radius(radius)
    import math
    return math.pi * radius ** 2

if __name__ == '__main__':
    kite_d1 = 4
    kite_d2 = 6
    circle_radius = 5 / 2
    total_area = kite_area(kite_d1, kite_d2) + circle_area(circle_radius)
    print(total_area)