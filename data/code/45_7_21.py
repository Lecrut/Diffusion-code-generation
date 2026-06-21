import math
PI = 3.141592653589793

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError('Radius must be a number.')
    if radius < 0:
        raise ValueError('Radius cannot be negative.')
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radius = 4.5
    area = calculate_circle_area(sample_radius)
    print(area)