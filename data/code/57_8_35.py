class Shape:
    SHAPE_RECTANGLE = 'rectangle'
    SHAPE_TRIANGLE = 'triangle'

    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
        if self.shape_type not in [Shape.SHAPE_RECTANGLE, Shape.SHAPE_TRIANGLE]:
            raise ValueError('Unsupported shape type')

    def area(self, *args):
        if self.shape_type == Shape.SHAPE_RECTANGLE:
            return self._calculate_rectangle_area(*args)
        elif self.shape_type == Shape.SHAPE_TRIANGLE:
            return self._calculate_triangle_area(*args)

    def _calculate_rectangle_area(self, width, height):
        if len(args) != 2:
            raise ValueError('Rectangle requires two arguments: width and height')
        return width * height

    def _calculate_triangle_area(self, base, height):
        if len(args) != 2:
            raise ValueError('Triangle requires two arguments: base and height')
        return 0.5 * base * height
if __name__ == '__main__':
    rectangle = Shape(Shape.SHAPE_RECTANGLE)
    print(rectangle.area(4, 5))
    triangle = Shape(Shape.SHAPE_TRIANGLE)
    print(triangle.area(3, 6))