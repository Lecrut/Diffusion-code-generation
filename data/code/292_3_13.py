import math

def calculate_circle_perimeter(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 5.0
    try:
        result = calculate_circle_perimeter(sample_radius)
        print(result)
    except ValueError as e:
        print(e)