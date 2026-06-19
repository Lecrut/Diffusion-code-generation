import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = [3.5, 7.0, -1, "invalid"]
    for radius in sample_values:
        try:
            area = calculate_circle_area(radius)
            print(f"Area of circle with radius {radius}: {area}")
        except (TypeError, ValueError) as e:
            print(f"Error calculating area for radius {radius}: {e}")