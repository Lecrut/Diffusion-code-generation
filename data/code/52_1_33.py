import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radii = [2.5, 6.0, 12.3]
    for index, radius in enumerate(sample_radii, start=1):
        area = calculate_circle_area(radius)
        print(f"Area of circle {index} with radius {radius}: {area}")