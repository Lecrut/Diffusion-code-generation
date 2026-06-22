import math

def calculate_circle_area(radius):
    if not validate_radius(radius):
        raise ValueError("Radius cannot be negative")
    return compute_area(radius)

def validate_radius(radius):
    return radius >= 0

def compute_area(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 15
    area = calculate_circle_area(sample_radius)
    print(area)