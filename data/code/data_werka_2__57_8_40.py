class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
        if self.shape_type not in ['rectangle', 'triangle']:
            raise ValueError('Unsupported shape type')

    def area(self, *args):
        if self.shape_type == 'rectangle':
            return self._calculate_rectangle_area(*args)
        elif self.shape_type == 'triangle':
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
    rectangle = Shape('rectangle')
    triangle = Shape('triangle')

    rect_width = 10
    rect_height = 5
    tri_base = 8
    tri_height = 4

    print(f"Rectangle area with width {rect_width} and height {rect_height}: {rectangle.area(rect_width, rect_height)}")
    print(f"Triangle area with base {tri_base} and height {tri_height}: {triangle.area(tri_base, tri_height)}")