import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {
        'small': 2.5,
        'medium': 6.0,
        'large': 15.0
    }
    for description, radius in sample_values.items():
        area = calculate_circle_area(radius)
        print(f"Area of {description} circle with radius {radius}: {area}")