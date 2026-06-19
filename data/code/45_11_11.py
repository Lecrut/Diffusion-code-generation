import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius < 0:
            raise ValueError('Radius cannot be negative')
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    radius_value = 3.0
    circle = Circle(radius_value)
    try:
        area = circle.area()
        print(f"The area of the circle with radius {radius_value} is {area:.2f}")
    except ValueError as e:
        print(e)