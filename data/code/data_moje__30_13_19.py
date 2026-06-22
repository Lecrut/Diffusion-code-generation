import math

def calculate_circle_area(radius):
    squared = radius * radius
    return math.pi * squared

if __name__ == '__main__':
    sample_radius = 7.0
    result = calculate_circle_area(sample_radius)
    print(result)