class ShapeAreaCalculator:

    def __init__(self):
        self.shapes = {'triangle': self._triangle_area, 'rectangle': self._rectangle_area, 'square': self._square_area, 'circle': self._circle_area}

    def calculate_area(self, shape, base=None, height=None, side=None, radius=None):
        if shape not in self.shapes:
            raise ValueError(f'Unknown shape: {shape}')
        area_func = self.shapes[shape]
        return area_func(base=base, height=height, side=side, radius=radius)

    def _triangle_area(self, base, height):
        if base is None or height is None:
            raise ValueError("Triangle requires both 'base' and 'height'")
        return 0.5 * base * height

    def _rectangle_area(self, length, width):
        if length is None or width is None:
            raise ValueError("Rectangle requires both 'length' and 'width'")
        return length * width

    def _square_area(self, side):
        if side is None:
            raise ValueError("Square requires 'side'")
        return side * side

    def _circle_area(self, radius):
        if radius is None:
            raise ValueError("Circle requires 'radius'")
        import math
        return math.pi * radius ** 2
if __name__ == '__main__':
    calculator = ShapeAreaCalculator()
    print(calculator.calculate_area('triangle', base=10, height=5))
    print(calculator.calculate_area('rectangle', length=4, width=6))
    print(calculator.calculate_area('square', side=3))
    print(calculator.calculate_area('circle', radius=7))