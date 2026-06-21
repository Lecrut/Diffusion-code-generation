import math
PI = math.pi

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radii = [2.0, 5.5, 12.3]
    for radius in sample_radii:
        area = calculate_circle_area(radius)
        print(f'The area of the circle with radius {radius} is: {area}')