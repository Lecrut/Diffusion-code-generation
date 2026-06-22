import math

def calculate_circumference(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 3.14
    try:
        circumference = calculate_circumference(sample_radius)
        print(circumference)
    except ValueError as e:
        print(e)