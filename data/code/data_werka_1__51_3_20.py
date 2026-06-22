import math
PI = math.pi

def calculate_circle_perimeter(radius):
    return 2 * PI * radius
if __name__ == '__main__':
    SAMPLE_RADIUS = 15
    perimeter = calculate_circle_perimeter(SAMPLE_RADIUS)
    print(perimeter)