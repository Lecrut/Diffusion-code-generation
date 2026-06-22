import math

def calculate_circle_perimeter(radius):
    if not isinstance(radius, (int, float)) or radius <= 0:
        raise ValueError("Radius must be a positive number")
    return 2 * math.pi * radius

if __name__ == '__main__':
    try:
        print(calculate_circle_perimeter(100))
    except ValueError as e:
        print(e)