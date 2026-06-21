import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        circle = Circle(3.5)
        print(f"The area of the circle is: {circle.area()}")
    except ValueError as e:
        print(e)