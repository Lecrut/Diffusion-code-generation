import math

def calculate_area_circle(radius):
    area = math.pi * radius ** 2
    return area

if __name__ == '__main__':
    sample_radius = 7.5
    circle_area = calculate_area_circle(sample_radius)
    print(circle_area)