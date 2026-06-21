import math

def calculate_circle_area(radius):
    if radius < 0:
        return None
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 5.0
    area = calculate_circle_area(sample_radius)
    print(area)