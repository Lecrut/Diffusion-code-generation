class Shape:

    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
        if self.shape_type not in ['rectangle', 'triangle']:
            raise ValueError('Unsupported shape type')

    def area(self, *args):
        try:
            if self.shape_type == 'rectangle':
                return self._calculate_rectangle_area(*args)
            elif self.shape_type == 'triangle':
                return self._calculate_triangle_area(*args)
        except TypeError as e:
            raise ValueError(f'Invalid arguments for {self.shape_type}: {e}')

    def _calculate_rectangle_area(self, width, height):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError('Width and height must be numbers')
        return width * height

    def _calculate_triangle_area(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError('Base and height must be numbers')
        return 0.5 * base * height
if __name__ == '__main__':
    rectangle = Shape('rectangle')
    print(rectangle.area(4, 5))
    triangle = Shape('triangle')
    print(triangle.area(3, 6))