import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radii = [2.0, 6.3, 12.5]
    for radius in sample_radii:
        area = calculate_circle_area(radius)
        print(f"Area of circle with radius {radius}: {area}")