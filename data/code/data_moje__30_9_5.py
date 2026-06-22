import math

PI_CONST = math.pi
AREA_MULTIPLIER = 2

def calculate_circle_area(radius):
    squared = radius ** AREA_MULTIPLIER
    return PI_CONST * squared

if __name__ == '__main__':
    sample_radius = 12.5
    area_value = calculate_circle_area(sample_radius)
    print(area_value)