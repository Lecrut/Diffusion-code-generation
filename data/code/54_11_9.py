import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius_values = [2.5, 6.0, 12.3]
    for radius in sample_radius_values:
        try:
            area = calculate_circle_area(radius)
            print(f"The area of a circle with radius {radius} is {area}")
        except ValueError as e:
            print(e)