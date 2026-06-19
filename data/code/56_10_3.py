import math

class Shapes:
    def __init__(self, radius=0, side_length=0):
        self.radius = radius
        self.side_length = side_length

    def circle_area(self):
        return math.pi * (self.radius ** 2)

    def circle_perimeter(self):
        return 2 * math.pi * self.radius

    def square_area(self):
        return self.side_length ** 2

    def square_perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    shape = Shapes(radius=5, side_length=10)
    print("Circle Area:", shape.circle_area())
    print("Circle Perimeter:", shape.circle_perimeter())
    print("Square Area:", shape.square_area())
    print("Square Perimeter:", shape.square_perimeter())