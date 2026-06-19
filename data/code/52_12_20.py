import math

class ShapeAreaCalculator:

    def __init__(self):
        self.shapes = {'rectangle': self._calculate_rectangle_area, 'circle': self._calculate_circle_area, 'triangle': self._calculate_triangle_area}

    def _validate_parameters(self, shape_type, **kwargs):
        required_params = {'rectangle': ['width', 'height'], 'circle': ['radius'], 'triangle': ['base', 'height']}
        missing_params = [param for param in required_params.get(shape_type, []) if kwargs.get(param) is None]
        if missing_params:
            raise ValueError(f"Missing required parameters for {shape_type}: {', '.join(missing_params)}")

    def _calculate_rectangle_area(self, width, height):
        return width * height

    def _calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def _calculate_triangle_area(self, base, height):
        return 0.5 * base * height

    def calculate_area(self, shape_type, **kwargs):
        area_function = self.shapes.get(shape_type)
        if area_function is None:
            raise ValueError(f'Unsupported shape type: {shape_type}')
        self._validate_parameters(shape_type, **kwargs)
        return area_function(**kwargs)
if __name__ == '__main__':
    calculator = ShapeAreaCalculator()
    try:
        print(calculator.calculate_area('rectangle', width=4, height=6))
        print(calculator.calculate_area('circle', radius=5))
        print(calculator.calculate_area('triangle', base=3, height=8))
        print(calculator.calculate_area('square', side=2))
    except ValueError as e:
        print(e)