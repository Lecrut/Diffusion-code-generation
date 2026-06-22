import math
PI = math.pi

def compute_circle_perimeter(radius):
    return 2 * PI * radius
if __name__ == '__main__':
    SAMPLE_RADIUS = 10.0
    result_perimeter = compute_circle_perimeter(SAMPLE_RADIUS)
    print(result_perimeter)