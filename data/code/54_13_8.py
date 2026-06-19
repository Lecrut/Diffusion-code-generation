import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number.")
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")

def calculate_circle_area(radius):
    validate_radius(radius)
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 3.5
    try:
        area = calculate_circle_area(sample_radius)
        print(area)
    except Exception as e:
        print(e)