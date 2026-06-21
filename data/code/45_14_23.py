import math
PI = math.pi

def calculate_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radius = 6
    area = calculate_area(sample_radius)
    print(area)