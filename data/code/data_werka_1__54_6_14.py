import math
PI = math.pi

def calculate_circle_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radius = 3
    area_result = calculate_circle_area(sample_radius)
    print(area_result)