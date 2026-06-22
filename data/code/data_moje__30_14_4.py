import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius

if __name__ == "__main__":
    sample_radii = [1, 2.5, 10]
    for r in sample_radii:
        print(calculate_circle_area(r))