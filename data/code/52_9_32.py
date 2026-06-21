import math
PI = math.pi

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radii = [1.5, 4.0, 10.0]
    for radius in sample_radii:
        try:
            area = calculate_circle_area(radius)
            print(f'The area of a circle with radius {radius} is: {area:.2f}')
        except ValueError as e:
            print(e)