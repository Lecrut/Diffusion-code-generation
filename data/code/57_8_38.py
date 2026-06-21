class Shape:
    RECTANGLE = 'rectangle'
    TRIANGLE = 'triangle'

    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
        if self.shape_type not in [Shape.RECTANGLE, Shape.TRIANGLE]:
            raise ValueError('Unsupported shape type')

    @staticmethod
    def _calculate_rectangle_area(width, height):
        return width * height

    @staticmethod
    def _calculate_triangle_area(base, height):
        return 0.5 * base * height

    def area(self, *args):
        if self.shape_type == Shape.RECTANGLE:
            if len(args) != 2:
                raise ValueError('Rectangle requires two arguments: width and height')
            width, height = args
            return Shape._calculate_rectangle_area(width, height)
        elif self.shape_type == Shape.TRIANGLE:
            if len(args) != 2:
                raise ValueError('Triangle requires two arguments: base and height')
            base, height = args
            return Shape._calculate_triangle_area(base, height)
if __name__ == '__main__':
    rectangle = Shape(Shape.RECTANGLE)
    print(rectangle.area(4, 5))
    triangle = Shape(Shape.TRIANGLE)
    print(triangle.area(3, 6))