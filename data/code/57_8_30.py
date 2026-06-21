class Shape:
    RECTANGLE = 'rectangle'
    TRIANGLE = 'triangle'

    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
        if self.shape_type not in [Shape.RECTANGLE, Shape.TRIANGLE]:
            raise ValueError(f'Unsupported shape type: {shape_type}')

    def area(self, *args):
        if self.shape_type == Shape.RECTANGLE:
            return self._calculate_rectangle_area(*args)
        elif self.shape_type == Shape.TRIANGLE:
            return self._calculate_triangle_area(*args)

    @staticmethod
    def _calculate_rectangle_area(width, height):
        if len(args) != 2:
            raise ValueError('Rectangle requires two arguments: width and height')
        return width * height

    @staticmethod
    def _calculate_triangle_area(base, height):
        if len(args) != 2:
            raise ValueError('Triangle requires two arguments: base and height')
        return 0.5 * base * height
if __name__ == '__main__':
    rectangle = Shape(Shape.RECTANGLE)
    print(rectangle.area(4, 5))
    triangle = Shape(Shape.TRIANGLE)
    print(triangle.area(3, 6))