import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def get_radius(self):
        return self.radius

if __name__ == '__main__':
    try:
        circle1 = Circle(4)
        print(circle1.calculate_perimeter())
        print(circle1.get_radius())

        circle2 = Circle(9)
        print(circle2.calculate_perimeter())
        print(circle2.get_radius())
    except ValueError as e:
        print(e)