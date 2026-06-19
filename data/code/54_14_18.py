import math
FIXED_RADIUS = 10.0

class Circle:

    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise ValueError('Radius cannot be negative')

    def area(self):
        return math.pi * self.radius ** 2

def calculate_circle_area(radius):
    circle = Circle(radius)
    return circle.area()
if __name__ == '__main__':
    try:
        radius_value = FIXED_RADIUS
        area_result = calculate_circle_area(radius_value)
        print(f'The area of the circle with radius {radius_value} is: {area_result}')
    except ValueError as e:
        print(e)