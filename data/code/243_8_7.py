import math

def calculate_perimeter(radius):
    if radius <= 0:
        raise ValueError("Radius must be greater than zero")
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 10
    try:
        perimeter = calculate_perimeter(sample_radius)
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(e)