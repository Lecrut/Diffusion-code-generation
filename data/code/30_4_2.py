import math

def calculate_circle_area(radius):
    squared_radius = radius * radius
    area = math.pi * squared_radius
    return area

if __name__ == '__main__':
    sample_radius = 7
    result = calculate_circle_area(sample_radius)
    print(result)