import math
PI = math.pi

def calculate_area_circle(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radius = 7.5
    area = calculate_area_circle(sample_radius)
    print(area)