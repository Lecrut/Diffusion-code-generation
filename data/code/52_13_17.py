import math
PI = math.pi

def calculate_circle_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    SAMPLE_RADIUS = 3
    area = calculate_circle_area(SAMPLE_RADIUS)
    print(area)