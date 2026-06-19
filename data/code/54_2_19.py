import math
PI = math.pi

def get_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    test_radii = [2.5, 10.0, 3.75]
    for radius in test_radii:
        area = get_area(radius)
        print(f'The area of a circle with radius {radius} is {area}')