def validate_diagonal(diagonal):
    if diagonal <= 0:
        raise ValueError("Diagonal must be greater than zero")

def calculate_kite_area(d1, d2):
    validate_diagonal(d1)
    validate_diagonal(d2)
    return 0.5 * d1 * d2

def validate_radius(radius):
    if radius <= 0:
        raise ValueError("Radius must be greater than zero")

def calculate_circle_area(radius):
    validate_radius(radius)
    import math
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    kite_d1 = 4
    kite_d2 = 6
    circle_radius = 5 / 2

    total_area = calculate_kite_area(kite_d1, kite_d2) + calculate_circle_area(circle_radius)
    print(total_area)