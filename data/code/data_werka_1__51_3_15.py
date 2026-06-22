import math

def calculate_circle_perimeter(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 4.5
    try:
        perimeter = calculate_circle_perimeter(sample_radius)
        print(perimeter)
    except ValueError as e:
        print(e)