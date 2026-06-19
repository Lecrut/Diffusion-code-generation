class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
        self.area_calculators = {
            'rectangle': lambda width, height: width * height,
            'triangle': lambda base, height: 0.5 * base * height
        }

    def area(self, *args):
        calculator = self.area_calculators.get(self.shape_type)
        if calculator:
            return calculator(*args)
        else:
            raise ValueError('Unsupported shape type')

if __name__ == '__main__':
    rectangle = Shape('rectangle')
    triangle = Shape('triangle')

    rect_area = rectangle.area(10, 5)
    tri_area = triangle.area(10, 5)

    print(f"Rectangle area: {rect_area}")
    print(f"Triangle area: {tri_area}")