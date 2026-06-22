import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 5.5
    try:
        area = calculate_circle_area(sample_radius)
        print(f"Area of circle with radius {sample_radius}: {area}")
    except ValueError as e:
        print(e)