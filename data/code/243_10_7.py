import math

def calculate_circle_perimeter(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * math.pi * radius

if __name__ == '__main__':
    try:
        sample_radius = -5.0
        print(calculate_circle_perimeter(sample_radius))
    except ValueError as e:
        print(e)