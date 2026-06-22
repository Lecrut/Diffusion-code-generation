class Shape:

    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
        if self.shape_type not in ['rectangle', 'triangle']:
            raise ValueError('Unsupported shape type')

    def area(self, *args):
        area_calculators = {'rectangle': self._calculate_rectangle_area, 'triangle': self._calculate_triangle_area}
        calculator = area_calculators.get(self.shape_type)
        if calculator:
            return calculator(*args)
        else:
            raise ValueError(f'Unsupported shape type: {self.shape_type}')

    def _calculate_rectangle_area(self, width, height):
        return width * height

    def _calculate_triangle_area(self, base, height):
        return 0.5 * base * height
if __name__ == '__main__':
    rectangle = Shape('rectangle')
    print(rectangle.area(5, 10))
    triangle = Shape('triangle')
    print(triangle.area(6, 8))