import math

CIRCLE_CONSTANT = math.pi

def calculate_circle_area(radius):
    return CIRCLE_CONSTANT * radius * radius

if __name__ == '__main__':
    sample_radius = 7.5
    computed_area = calculate_circle_area(sample_radius)
    print(computed_area)