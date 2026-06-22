import math
PI = math.pi

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radii = [6.0, 12.3, 0.0]
    for radius in sample_radii:
        try:
            area = calculate_circle_area(radius)
            print(f'The area of the circle with radius {radius} is: {area}')
        except ValueError as e:
            print(e)