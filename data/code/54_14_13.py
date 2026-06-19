import math

class Circle:
    PI = math.pi

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    @staticmethod
    def area(radius):
        return Circle.PI * radius ** 2

if __name__ == '__main__':
    try:
        radius_value = 10.0
        circle_area = Circle.area(radius_value)
        print(f"The area of the circle with radius {radius_value} is {circle_area}")
    except ValueError as e:
        print(e)