import math
PI = math.pi

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radii = [4, 9, 16]
    for index, radius in enumerate(sample_radii, start=1):
        try:
            area = calculate_circle_area(radius)
            print(f'Sample {index}: The area of a circle with radius {radius} is {area:.2f}')
        except ValueError as e:
            print(e)