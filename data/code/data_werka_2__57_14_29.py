import math

PI = math.pi
MIN_RADIUS = 0.0

def calculate_circle_area(radius):
    if radius < MIN_RADIUS:
        raise ValueError("Radius cannot be negative")
    return PI * radius ** 2

if __name__ == '__main__':
    sample_radius = 4.5
    area = calculate_circle_area(sample_radius)
    print(area)