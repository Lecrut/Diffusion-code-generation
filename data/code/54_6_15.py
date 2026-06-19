import math

def compute_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 8
    area_result = compute_circle_area(sample_radius)
    print(area_result)