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
    sample_values = [5.5, 10.0, -3.0, 'a']
    for value in sample_values:
        try:
            area = calculate_circle_area(value)
            print(f"The area of the circle with radius {value} is {area:.2f}")
        except (TypeError, ValueError) as e:
            print(e)