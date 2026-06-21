import math

class Shapes:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type.lower()
        if self.shape_type == 'circle':
            self.radius = kwargs.get('radius')
        elif self.shape_type == 'square':
            self.side_length = kwargs.get('side_length')
        else:
            raise ValueError("Unsupported shape type")

    def area(self):
        if self.shape_type == 'circle':
            return math.pi * (self.radius ** 2)
        elif self.shape_type == 'square':
            return self.side_length ** 2

    def perimeter(self):
        if self.shape_type == 'circle':
            return 2 * math.pi * self.radius
        elif self.shape_type == 'square':
            return 4 * self.side_length

if __name__ == '__main__':
    circle = Shapes(shape_type='circle', radius=5)
    square = Shapes(shape_type='square', side_length=10)

    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())
    print("Square Area:", square.area())
    print("Square Perimeter:", square.perimeter())