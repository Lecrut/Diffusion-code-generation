import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radii = [0, 1, 5, 10.5]
    for r in sample_radii:
        try:
            area = calculate_circle_area(r)
            print(f"Radius: {r}, Area: {area}")
        except (TypeError, ValueError) as e:
            print(f"Radius: {r}, Error: {e}")