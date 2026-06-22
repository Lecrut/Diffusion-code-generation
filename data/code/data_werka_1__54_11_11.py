import math
PI = math.pi

def calculate_circle_area(radius):
    return PI * radius ** 2
if __name__ == '__main__':
    RADIUS_VALUES = [5.0, 10.0, 15.0]
    for radius in RADIUS_VALUES:
        area = calculate_circle_area(radius)
        print(f'The area of a circle with radius {radius} is {area}')