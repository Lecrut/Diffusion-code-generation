import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius

if __name__ == '__main__':
    sample_radii = [5, 0, 3.14, -1]
    for r in sample_radii:
        try:
            area = calculate_circle_area(r)
            print(area)
        except ValueError as e:
            print(repr(e))