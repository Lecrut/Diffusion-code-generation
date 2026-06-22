import math

def calculate_circle_area(radius):
    try:
        radius = float(radius)
    except (TypeError, ValueError):
        raise TypeError("Radius must be a numeric value")
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    print(calculate_circle_area(5))
    print(calculate_circle_area(0))
    try:
        calculate_circle_area("abc")
    except TypeError as e:
        print(str(e))
    try:
        calculate_circle_area(-3)
    except ValueError as e:
        print(str(e))
    print(calculate_circle_area(2.5))