class Shape:
    RECTANGLE = 'rectangle'
    TRIANGLE = 'triangle'

    def __init__(self, shape_type):
        if shape_type not in (Shape.RECTANGLE, Shape.TRIANGLE):
            raise ValueError("Unsupported shape type")
        self.shape_type = shape_type

    def calculate_area(self, *args):
        if self.shape_type == Shape.RECTANGLE:
            if len(args) != 2:
                raise ValueError('Rectangle requires two arguments: width and height')
            width, height = args
            return width * height
        elif self.shape_type == Shape.TRIANGLE:
            if len(args) != 2:
                raise ValueError('Triangle requires two arguments: base and height')
            base, height = args
            return 0.5 * base * height

if __name__ == '__main__':
    rectangle = Shape(Shape.RECTANGLE)
    rect_area = rectangle.calculate_area(10, 5)
    print(f"Rectangle Area: {rect_area}")

    triangle = Shape(Shape.TRIANGLE)
    tri_area = triangle.calculate_area(8, 4)
    print(f"Triangle Area: {tri_area}")