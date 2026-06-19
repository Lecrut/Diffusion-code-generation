import math

class ShapeCalculator:
    def __init__(self):
        self.shapes = {
            'rectangle': self.rectangle_area,
            'circle': self.circle_area,
            'triangle': self.triangle_area
        }

    def calculate(self, shape_type, **kwargs):
        area_function = self.shapes.get(shape_type)
        if area_function is None:
            raise ValueError(f'Unsupported shape type: {shape_type}')
        
        missing_params = [param for param in area_function.__code__.co_varnames[1:] if kwargs.get(param) is None]
        if missing_params:
            raise ValueError(f"Missing required parameters for {shape_type}: {', '.join(missing_params)}")
        
        return area_function(**kwargs)

    @staticmethod
    def rectangle_area(width, height):
        return width * height

    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    calculator = ShapeCalculator()
    try:
        print(calculator.calculate('rectangle', width=5, height=10))
        print(calculator.calculate('circle', radius=7))
        print(calculator.calculate('triangle', base=6, height=4))
        print(calculator.calculate('square', side=3))
    except ValueError as e:
        print(e)