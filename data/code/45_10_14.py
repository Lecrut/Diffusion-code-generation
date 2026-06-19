import math
PI = math.pi

def calculate_circle_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    SAMPLE_RADIUS = 15.0
    area_result = calculate_circle_area(SAMPLE_RADIUS)
    print(area_result)