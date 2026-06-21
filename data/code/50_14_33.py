import math

def is_valid_radius(radius):
    return isinstance(radius, (int, float)) and radius >= 0

def compute_circle_area(radius):
    if not is_valid_radius(radius):
        raise ValueError("Radius must be a non-negative number.")
    return math.pi * radius ** 2

def compute_area_difference(radius1, radius2):
    area1 = compute_circle_area(radius1)
    area2 = compute_circle_area(radius2)
    return abs(area1 - area2)

if __name__ == '__main__':
    sample_radius1 = 8.0
    sample_radius2 = 3.5
    area_difference = compute_area_difference(sample_radius1, sample_radius2)
    print(area_difference)