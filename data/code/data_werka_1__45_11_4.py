import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    circle_radius = 3.0
    my_circle = Circle(circle_radius)
    print(f"The area of the circle with radius {circle_radius} is {my_circle.area():.2f}")