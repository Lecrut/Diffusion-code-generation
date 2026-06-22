import math

class Circle:

    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('Radius must be a number')
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
if __name__ == '__main__':
    try:
        circle1 = Circle(5.0)
        area1 = circle1.calculate_area()
        print(f'Area of circle with radius 5.0: {area1}')
        circle2 = Circle(-3.0)
        area2 = circle2.calculate_area()
        print(f'Area of circle with radius -3.0: {area2}')
    except (TypeError, ValueError) as e:
        print(e)