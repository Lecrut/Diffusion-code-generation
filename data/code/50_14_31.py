import math

def compute_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * (radius ** 2)

def compute_absolute_area_difference(radius1, radius2):
    area1 = compute_circle_area(radius1)
    area2 = compute_circle_area(radius2)
    return abs(area1 - area2)

if __name__ == '__main__':
    sample_radius1 = 6.0
    sample_radius2 = 4.0
    try:
        difference = compute_absolute_area_difference(sample_radius1, sample_radius2)
        print(difference)
    except ValueError as e:
        print(e)