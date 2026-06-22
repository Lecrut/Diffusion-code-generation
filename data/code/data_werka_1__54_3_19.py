import math

def calculate_circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radii = [5.0, 0.5, 10.5]
    for radius in sample_radii:
        area = calculate_circle_area(radius)
        print(f"The area of a circle with radius {radius} is {area}")