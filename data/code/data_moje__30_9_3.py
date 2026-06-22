import math

def calculate_circle_area(radius):
    if radius < 0:
        return 0.0
    return math.pi * radius * radius

if __name__ == '__main__':
    sample_radius = 7
    result = calculate_circle_area(sample_radius)
    print(result)