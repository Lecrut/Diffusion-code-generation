import math

def is_valid_radius(radius):
    return radius >= 0

def calculate_circle_perimeter(radius):
    if not is_valid_radius(radius):
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 5
    try:
        perimeter = calculate_circle_perimeter(sample_radius)
        print(perimeter)
    except ValueError as e:
        print(e)