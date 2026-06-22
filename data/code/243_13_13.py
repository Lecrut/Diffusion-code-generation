import math

def calculate_circle_perimeter(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return 2 * math.pi * radius

if __name__ == '__main__':
    try:
        sample_radius = 10.5
        perimeter = calculate_circle_perimeter(sample_radius)
        print(perimeter)
    except ValueError as e:
        print(e)