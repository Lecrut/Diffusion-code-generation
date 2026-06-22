import math

def calculate_circle_area(radius):
    squared_radius = radius * radius
    return math.pi * squared_radius

if __name__ == '__main__':
    sample_radius = 12
    result = calculate_circle_area(sample_radius)
    print(result)