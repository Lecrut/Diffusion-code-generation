import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a numeric type.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2

if __name__ == '__main__':
    print(calculate_circle_area(5))
    print(calculate_circle_area(0))
    try:
        calculate_circle_area(-3)
    except ValueError:
        print("Handled negative radius")
    try:
        calculate_circle_area("abc")
    except TypeError:
        print("Handled non-numeric input")
    print(calculate_circle_area(2.5))