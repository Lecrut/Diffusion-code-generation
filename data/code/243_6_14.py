import math

CIRCLE_RADIUS = 100
PERIMETER_FORMULA = lambda r: 2 * math.pi * r

def calculate_circle_perimeter():
    radius = CIRCLE_RADIUS
    perimeter = PERIMETER_FORMULA(radius)
    return float(perimeter)

if __name__ == '__main__':
    print(calculate_circle_perimeter())