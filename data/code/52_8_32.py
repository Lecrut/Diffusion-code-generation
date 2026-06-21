import math

class ShapeCalculator:

    def __init__(self):
        self.shapes = {'rectangle': self.rectangle_area, 'circle': self.circle_area, 'triangle': self.triangle_area}

    def calculate(self, shape_type, *args):
        if shape_type not in self.shapes:
            raise ValueError(f'Unsupported shape type: {shape_type}')
        area_function = self.shapes[shape_type]
        return area_function(*args)

    def rectangle_area(self, width, height):
        if len(args) != 2:
            raise ValueError('Rectangle requires two parameters: width and height')
        return width * height

    def circle_area(self, radius):
        if len(args) != 1:
            raise ValueError('Circle requires one parameter: radius')
        return math.pi * radius ** 2

    def triangle_area(self, base, height):
        if len(args) != 3:
            raise ValueError('Triangle requires three parameters: base and height')
        return 0.5 * base * height
if __name__ == '__main__':
    calculator = ShapeCalculator()
    try:
        print(calculator.calculate('rectangle', 4, 5))
        print(calculator.calculate('circle', 3))
        print(calculator.calculate('triangle', 6, 4))
        print(calculator.calculate('square', 5))
    except ValueError as e:
        print(e)