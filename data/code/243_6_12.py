import math

CIRCLE_RADIUS = 100
CIRCLE_PERIMETER_FORMULA = lambda r: 2 * math.pi * r

def calculate_circle_perimeter():
    radius = CIRCLE_RADIUS
    perimeter = CIRCLE_PERIMETER_FORMULA(radius)
    return float(perimeter)

if __name__ == '__main__':
    print(calculate_circle_perimeter())