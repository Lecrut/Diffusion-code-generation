import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * (radius ** 2)

def compute_area_difference(radius1, radius2):
    area1 = calculate_circle_area(radius1)
    area2 = calculate_circle_area(radius2)
    return abs(area1 - area2)

if __name__ == '__main__':
    sample_radius1 = 10.0
    sample_radius2 = 4.5
    difference = compute_area_difference(sample_radius1, sample_radius2)
    print(difference)