import math

def calculate_area_of_circle(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 3
    result = calculate_area_of_circle(sample_radius)
    print(result)