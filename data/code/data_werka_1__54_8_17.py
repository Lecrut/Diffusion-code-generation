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
    sample_values = {
        'small': 1.0,
        'medium': 5.5,
        'large': 10.0
    }
    for size, radius in sample_values.items():
        try:
            area = calculate_circle_area(radius)
            print(f"The area of a circle with {size} radius ({radius}) is: {area}")
        except (TypeError, ValueError) as e:
            print(e)