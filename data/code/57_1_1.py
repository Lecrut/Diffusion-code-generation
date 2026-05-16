import math
def calculate_area_circle(radius):
    return math.pi * radius**2
if __name__ == '__main__':
    sample_radius = 5.0
    area = calculate_area_circle(sample_radius)
    print(area)