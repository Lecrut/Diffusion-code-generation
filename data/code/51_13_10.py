import math
PI = math.pi

def compute_circle_perimeter(radius):
    return 2 * PI * radius
if __name__ == '__main__':
    RADIUS = 10.0
    perimeter = compute_circle_perimeter(RADIUS)
    print(perimeter)