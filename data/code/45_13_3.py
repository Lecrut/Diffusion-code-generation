import math

def calculate_circle_area(radius):
    squared_radius = radius * radius
    area_value = math.pi * squared_radius
    return area_value

if __name__ == '__main__':
    sample_radius = 5.0
    computed_area = calculate_circle_area(sample_radius)
    print(computed_area)