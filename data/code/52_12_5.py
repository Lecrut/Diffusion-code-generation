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
        
        missing_params = [param for param in kwargs.keys() if kwargs[param] is None]
        if missing_params:
            raise ValueError(f"Missing required parameters for {shape_type}: {', '.join(missing_params)}")
        
        return area_function(**kwargs)

    def rectangle_area(self, width=None, height=None):
        if width is None or height is None:
            raise ValueError('Width and height are required for rectangle.')
        return width * height

    def circle_area(self, radius=None):
        if radius is None:
            raise ValueError('Radius is required for circle.')
        return math.pi * radius ** 2

    def triangle_area(self, base=None, height=None):
        if base is None or height is None:
            raise ValueError('Base and height are required for triangle.')
        return 0.5 * base * height

if __name__ == '__main__':
    calculator = ShapeCalculator()
    print(calculator.calculate('rectangle', width=5, height=10))
    print(calculator.calculate('circle', radius=7))
    print(calculator.calculate('triangle', base=6, height=4))