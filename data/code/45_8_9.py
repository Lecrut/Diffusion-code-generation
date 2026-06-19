import math

class Circle:
    PI = math.pi

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return self.PI * (self.radius ** 2)

if __name__ == '__main__':
    try:
        circle = Circle(8)
        print(f"Area of circle with radius 8: {circle.area()}")
    except ValueError as e:
        print(e)