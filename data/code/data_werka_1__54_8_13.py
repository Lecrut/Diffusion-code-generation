import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def calculate_circle_area(radius):
    validate_radius(radius)
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = [1, 5, 10, -3, 'a']
    for value in sample_values:
        try:
            area = calculate_circle_area(value)
            print(f"The area of a circle with radius {value} is: {area}")
        except Exception as e:
            print(f"Error calculating area for radius {value}: {e}")