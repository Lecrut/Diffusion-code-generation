import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)) or radius < 0:
        raise ValueError("Radius must be a non-negative number")

def compute_circle_area(radius):
    return math.pi * radius ** 2

def compute_area_difference(radius1, radius2):
    validate_radius(radius1)
    validate_radius(radius2)
    area1 = compute_circle_area(radius1)
    area2 = compute_circle_area(radius2)
    return abs(area1 - area2)

if __name__ == '__main__':
    sample_radius1 = 10.5
    sample_radius2 = 4.2
    difference = compute_area_difference(sample_radius1, sample_radius2)
    print(difference)