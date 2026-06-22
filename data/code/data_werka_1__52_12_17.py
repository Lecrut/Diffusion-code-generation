import math

class ShapeAreaCalculator:

    def __init__(self):
        self.shapes = {'rectangle': self._calculate_rectangle_area, 'circle': self._calculate_circle_area, 'triangle': self._calculate_triangle_area}

    def calculate(self, shape_type, **kwargs):
        area_function = self.shapes.get(shape_type)
        if area_function is None:
            raise ValueError(f'Unsupported shape type: {shape_type}')
        required_params = {'rectangle': ['width', 'height'], 'circle': ['radius'], 'triangle': ['base', 'height']}
        missing_params = [param for param in required_params[shape_type] if kwargs.get(param) is None]
        if missing_params:
            raise ValueError(f"Missing required parameters for {shape_type}: {', '.join(missing_params)}")
        return area_function(**kwargs)

    def _calculate_rectangle_area(self, width, height):
        return width * height

    def _calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def _calculate_triangle_area(self, base, height):
        return 0.5 * base * height
if __name__ == '__main__':
    calculator = ShapeAreaCalculator()
    try:
        print(calculator.calculate('rectangle', width=5, height=10))
        print(calculator.calculate('circle', radius=7))
        print(calculator.calculate('triangle', base=6, height=4))
        print(calculator.calculate('square', side=3))
    except ValueError as e:
        print(e)