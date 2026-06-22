import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {
        'small': 1.0,
        'medium': 5.0,
        'large': 10.0
    }
    for size, radius in sample_values.items():
        area = calculate_circle_area(radius)
        print(f"Area of {size} circle with radius {radius}: {area}")