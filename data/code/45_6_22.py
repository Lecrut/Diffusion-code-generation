import math

def compute_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radii = [3, 7.5, 0, 12]
    for radius in sample_radii:
        try:
            area = compute_area(radius)
            print(f"Area of circle with radius {radius}: {area}")
        except ValueError as e:
            print(e)