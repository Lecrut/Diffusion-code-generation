import math

def validate_radius(radius):
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")

def calculate_circumference(radius):
    validate_radius(radius)
    return 2 * math.pi * radius

if __name__ == '__main__':
    try:
        result = calculate_circumference(7)
        print(f"Circumference for radius 7: {result}")
    except ValueError as e:
        print(f"Error caught: {e}")