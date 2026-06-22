import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    circle1 = Circle(5.0)
    circle2 = Circle(7.5)
    circle3 = Circle(10.0)

    print(f"The area of a circle with radius {circle1.radius} is {circle1.area()}")
    print(f"The area of a circle with radius {circle2.radius} is {circle2.area()}")
    print(f"The area of a circle with radius {circle3.radius} is {circle3.area()}")