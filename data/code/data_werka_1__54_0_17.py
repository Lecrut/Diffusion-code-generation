import math
PI = math.pi

def calculate_circle_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    sample_radii = [1, 2.5, 7]
    for radius in sample_radii:
        area = calculate_circle_area(radius)
        print(f'The area of a circle with radius {radius} is: {area}')