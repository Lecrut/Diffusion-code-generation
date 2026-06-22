import math

def calculate_circumference(radius):
    if not isinstance(radius, (int, float)) or radius < 0:
        raise ValueError("Radius must be a non-negative number")
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 5.0
    try:
        circumference = calculate_circumference(sample_radius)
        print(circumference)
    except ValueError as e:
        print(e)