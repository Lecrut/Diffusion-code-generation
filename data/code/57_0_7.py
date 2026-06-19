import math
PI = math.pi

def calculate_area_circle(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    SAMPLE_RADIUS = 7.5
    area = calculate_area_circle(SAMPLE_RADIUS)
    print(area)