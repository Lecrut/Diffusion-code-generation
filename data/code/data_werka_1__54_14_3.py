import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

def calculate_circle_area(radius):
    circle = Circle(radius)
    return circle.area()

if __name__ == '__main__':
    try:
        radius = 7.5
        area = calculate_circle_area(radius)
        print(area)
    except ValueError as e:
        print(e)