import math

CIRCLE_RADIUS = 100

def calculate_circle_perimeter(radius=CIRCLE_RADIUS):
    return float(2 * math.pi * radius)

if __name__ == '__main__':
    print(calculate_circle_perimeter())