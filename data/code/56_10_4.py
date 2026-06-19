import math

class Shapes:
    def __init__(self):
        self.shapes = {
            'circle': {'radius': 0},
            'square': {'side_length': 0}
        }

    def set_circle(self, radius):
        self.shapes['circle']['radius'] = radius

    def set_square(self, side_length):
        self.shapes['square']['side_length'] = side_length

    def circle_area(self):
        return math.pi * (self.shapes['circle']['radius'] ** 2)

    def circle_perimeter(self):
        return 2 * math.pi * self.shapes['circle']['radius']

    def square_area(self):
        return self.shapes['square']['side_length'] ** 2

    def square_perimeter(self):
        return 4 * self.shapes['square']['side_length']

if __name__ == '__main__':
    shape = Shapes()
    shape.set_circle(5.0)
    shape.set_square(10.0)
    print("Circle Area:", shape.circle_area())
    print("Circle Perimeter:", shape.circle_perimeter())
    print("Square Area:", shape.square_area())
    print("Square Perimeter:", shape.square_perimeter())