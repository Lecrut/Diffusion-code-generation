import math
PI = math.pi
SAMPLE_RADIUS = 3.5

def compute_circle_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    radius_value = SAMPLE_RADIUS
    computed_area = compute_circle_area(radius_value)
    print(f'The area of the circle with radius {radius_value} is {computed_area:.2f}')