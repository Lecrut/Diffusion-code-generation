import math
PI = math.pi

def calculate_area_of_circle(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radius = 10
    area_result = calculate_area_of_circle(sample_radius)
    print(area_result)