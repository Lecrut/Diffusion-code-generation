import math
PI = math.pi

def calculate_circle_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    SAMPLE_RADIUS_1 = 4.0
    SAMPLE_RADIUS_2 = 6.5
    print(f'Area of circle with radius {SAMPLE_RADIUS_1}: {calculate_circle_area(SAMPLE_RADIUS_1)}')
    print(f'Area of circle with radius {SAMPLE_RADIUS_2}: {calculate_circle_area(SAMPLE_RADIUS_2)}')