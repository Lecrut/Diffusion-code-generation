import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius must be non-negative")

def compute_circle_area(radius):
    validate_radius(radius)
    return math.pi * (radius ** 2)

def compute_area_difference(radius1, radius2):
    area1 = compute_circle_area(radius1)
    area2 = compute_circle_area(radius2)
    return abs(area1 - area2)

if __name__ == '__main__':
    sample_radius1 = 10.5
    sample_radius2 = 4.2
    difference = compute_area_difference(sample_radius1, sample_radius2)
    print(difference)