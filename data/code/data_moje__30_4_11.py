import math

CIRCLE_AREA_PI = math.pi

def compute_circle_area(radius):
    pi_factor = CIRCLE_AREA_PI
    radius_squared = radius * radius
    area = pi_factor * radius_squared
    return area

if __name__ == '__main__':
    sample_radius = 3.0
    computed_value = compute_circle_area(sample_radius)
    print(computed_value)