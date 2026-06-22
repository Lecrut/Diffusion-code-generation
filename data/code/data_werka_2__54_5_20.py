import math
PI = math.pi

class Circle:

    def __init__(self, radius):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

    def circumference(self):
        return 2 * PI * self.radius
if __name__ == '__main__':
    try:
        sample_radius = 7
        circle = Circle(sample_radius)
        print('Area:', circle.area())
        print('Circumference:', circle.circumference())
    except ValueError as e:
        print(e)