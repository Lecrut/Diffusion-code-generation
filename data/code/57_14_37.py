import math
PI = math.pi

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError('Radius must be a number')
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radius = 4.2
    try:
        area = calculate_circle_area(sample_radius)
        print(area)
    except (TypeError, ValueError) as e:
        print(e)