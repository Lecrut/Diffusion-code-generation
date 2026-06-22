import math
PI = math.pi

def compute_circle_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radii = [3, 7, 1.5, 0, -2]
    for radius in sample_radii:
        try:
            area = compute_circle_area(radius)
            print(f'Area of circle with radius {radius}: {area}')
        except ValueError as e:
            print(e)