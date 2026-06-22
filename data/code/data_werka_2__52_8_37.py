import math

class ShapeCalculator:

    def __init__(self):
        self.shapes = {'rectangle': self.rectangle_area, 'circle': self.circle_area, 'triangle': self.triangle_area}

    def calculate_area(self, shape_type, *args):
        if shape_type in self.shapes:
            return self.shapes[shape_type](*args)
        else:
            raise ValueError(f'Unsupported shape type: {shape_type}')

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
        print(calculator.calculate_area('rectangle', 5, 10))
        print(calculator.calculate_area('circle', 7))
        print(calculator.calculate_area('triangle', 8, 6))
        print(calculator.calculate_area('square', 4))
    except ValueError as e:
        print(e)