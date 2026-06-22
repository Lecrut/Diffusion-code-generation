import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    radius_values = [5, 0, 10]
    for r in radius_values:
        area = calculate_circle_area(r)
        print(area)