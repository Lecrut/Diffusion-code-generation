import math

CIRCLE_AREA_RADIUS_FACTOR = 2.0

def compute_circle_area(radius):
    return math.pi * (radius ** CIRCLE_AREA_RADIUS_FACTOR)

if __name__ == '__main__':
    sample_radius = 10
    area_result = compute_circle_area(sample_radius)
    print(area_result)