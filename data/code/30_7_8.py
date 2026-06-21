import math

def _square_radius(value):
    return value * value

def calculate_circle_area(radius):
    squared = _square_radius(radius)
    area = math.pi * squared
    return area

if __name__ == '__main__':
    sample_radius = 12.5
    result = calculate_circle_area(sample_radius)
    print(result)