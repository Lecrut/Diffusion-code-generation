import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a numeric value.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    test_radius = 5
    area = calculate_circle_area(test_radius)
    print(area)