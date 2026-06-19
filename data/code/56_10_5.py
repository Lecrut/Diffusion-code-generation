import math

class Shapes:
    def __init__(self, radius=None, side_length=None):
        if radius is not None and radius < 0:
            raise ValueError("Radius cannot be negative")
        if side_length is not None and side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.radius = radius
        self.side_length = side_length

    def circle_area(self):
        if self.radius is None:
            raise ValueError("Radius must be set to calculate area")
        return math.pi * (self.radius ** 2)

    def circle_perimeter(self):
        if self.radius is None:
            raise ValueError("Radius must be set to calculate perimeter")
        return 2 * math.pi * self.radius

    def square_area(self):
        if self.side_length is None:
            raise ValueError("Side length must be set to calculate area")
        return self.side_length ** 2

    def square_perimeter(self):
        if self.side_length is None:
            raise ValueError("Side length must be set to calculate perimeter")
        return 4 * self.side_length

if __name__ == '__main__':
    try:
        circle = Shapes(radius=5.0)
        print(f"Circle Area: {circle.circle_area()}")
        print(f"Circle Perimeter: {circle.circle_perimeter()}")

        square = Shapes(side_length=10.0)
        print(f"Square Area: {square.square_area()}")
        print(f"Square Perimeter: {square.square_perimeter()}")
    except ValueError as e:
        print(e)