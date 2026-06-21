import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    test_radius_positive = 5
    test_radius_negative = -3

    print(calculate_circle_area(test_radius_positive))

    try:
        print(calculate_circle_area(test_radius_negative))
    except ValueError as e:
        print(e)