import math

def get_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return math.pi * radius ** 2
if __name__ == '__main__':
    sample_radius = 5.0
    try:
        area = get_area(sample_radius)
        print(area)
    except ValueError as e:
        print(e)
    invalid_radius = -3.0
    try:
        area = get_area(invalid_radius)
        print(area)
    except ValueError as e:
        print(e)