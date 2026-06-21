import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius

if __name__ == '__main__':
    try:
        print(calculate_circle_area(5))
        print(calculate_circle_area(0))
        print(calculate_circle_area(3.14))
        try:
            calculate_circle_area("hello")
        except TypeError as e:
            print(str(e))
        try:
            calculate_circle_area(-2)
        except ValueError as e:
            print(str(e))
    except Exception as e:
        print(str(e))