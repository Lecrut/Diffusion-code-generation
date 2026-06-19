class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()

    def area(self, dimension1, dimension2):
        if self.shape_type == 'rectangle':
            return self._rectangle_area(dimension1, dimension2)
        elif self.shape_type == 'triangle':
            return self._triangle_area(dimension1, dimension2)
        else:
            raise ValueError('Unsupported shape type')

    def _rectangle_area(self, width, height):
        return width * height

    def _triangle_area(self, base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    rectangle = Shape('rectangle')
    rect_width = 7
    rect_height = 3
    rectangle_area = rectangle.area(rect_width, rect_height)
    print(f"Area of rectangle: {rectangle_area}")

    triangle = Shape('triangle')
    tri_base = 8
    tri_height = 4
    triangle_area = triangle.area(tri_base, tri_height)
    print(f"Area of triangle: {triangle_area}")