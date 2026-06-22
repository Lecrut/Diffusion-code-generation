import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radii = [0, 5, 10, -3]
    for r in sample_radii:
        try:
            area = calculate_circle_area(r)
            print(f"Radius: {r}, Area: {area}")
        except ValueError as e:
            print(f"Radius: {r}, Error: {e}")