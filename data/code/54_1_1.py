import math
def calculate_circle_area(radius):
    return math.pi * radius * radius
if __name__ == '__main__':
    sample_radius = 5.0
    area = calculate_circle_area(sample_radius)
    print(area)