import math
PI = math.pi

def compute_circle_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return PI * radius ** 2
if __name__ == '__main__':
    SAMPLE_RADIUS = 3
    try:
        area = compute_circle_area(SAMPLE_RADIUS)
        print(area)
    except ValueError as e:
        print(e)