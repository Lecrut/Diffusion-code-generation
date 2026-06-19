import math

def validate_radius(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return True

def calculate_circle_area(radius):
    validate_radius(radius)
    area = math.pi * radius ** 2
    return area

if __name__ == '__main__':
    sample_radius = 7.5
    area = calculate_circle_area(sample_radius)
    print(area)