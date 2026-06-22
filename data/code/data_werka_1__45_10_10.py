import math
PI = math.pi

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radius = 15.0
    try:
        area_result = calculate_circle_area(sample_radius)
        print(area_result)
    except ValueError as e:
        print(e)