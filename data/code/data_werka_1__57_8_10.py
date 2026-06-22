class AreaCalculator:
    def __init__(self):
        self.formulas = {
            'triangle': self._triangle_area,
            'rectangle': self._rectangle_area,
            'circle': self._circle_area,
            'square': self._square_area
        }

    def _triangle_area(self, base, height):
        return 0.5 * base * height

    def _rectangle_area(self, length, width):
        return length * width

    def _circle_area(self, radius):
        import math
        return math.pi * (radius ** 2)

    def _square_area(self, side):
        return side * side

    def calculate_area(self, shape, **kwargs):
        if shape not in self.formulas:
            raise ValueError(f"Unknown shape: {shape}")
        return self.formulas[shape](**kwargs)

if __name__ == '__main__':
    calculator = AreaCalculator()
    print(calculator.calculate_area('triangle', base=5, height=10))
    print(calculator.calculate_area('rectangle', length=4, width=3))
    print(calculator.calculate_area('circle', radius=7))
    print(calculator.calculate_area('square', side=6))