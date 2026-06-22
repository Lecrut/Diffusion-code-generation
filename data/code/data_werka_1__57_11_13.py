import math

def is_valid_radius(radius):
    return radius >= 0

def calculate_circle_area(radius):
    if not is_valid_radius(radius):
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radii = [2, 5, -1, 7.5]
    for radius in sample_radii:
        try:
            area = calculate_circle_area(radius)
            print(f"Area of circle with radius {radius}: {area}")
        except ValueError as e:
            print(e)