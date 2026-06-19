import math

def validate_radius(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def calculate_circle_perimeter(radius):
    validate_radius(radius)
    return 2 * math.pi * radius

if __name__ == '__main__':
    hard_coded_radius = 10.0
    try:
        circle_perimeter = calculate_circle_perimeter(hard_coded_radius)
        print(circle_perimeter)
    except ValueError as e:
        print(e)