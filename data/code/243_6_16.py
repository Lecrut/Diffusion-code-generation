import math

def calculate_circle_perimeter():
    radius = 100
    if not isinstance(radius, (int, float)) or radius <= 0:
        raise ValueError("Radius must be a positive number")
    perimeter = 2 * math.pi * radius
    return float(perimeter)

if __name__ == '__main__':
    try:
        print(calculate_circle_perimeter())
    except ValueError as e:
        print(e)