import math

def validate_radius(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return True

def calculate_circle_area(radius):
    if validate_radius(radius):
        return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 7
    area = calculate_circle_area(sample_radius)
    print(area)