import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    try:
        circle = Circle(radius=12)
        perimeter = circle.calculate_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)