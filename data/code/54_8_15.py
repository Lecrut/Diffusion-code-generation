import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {
        'tiny': 0.1,
        'small': 1,
        'medium': 5,
        'large': 10
    }
    for description, radius in sample_values.items():
        try:
            area = calculate_circle_area(radius)
            print(f"The area of a circle with {description} radius ({radius}) is: {area:.2f}")
        except (TypeError, ValueError) as e:
            print(f"Error calculating area for radius {radius}: {e}")