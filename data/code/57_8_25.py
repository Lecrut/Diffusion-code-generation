class Shape:

    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()

    def area(self, *args):
        if self.shape_type == 'rectangle':
            if len(args) != 2:
                raise ValueError('Rectangle requires two arguments: width and height')
            width, height = args
            return width * height
        elif self.shape_type == 'triangle':
            if len(args) != 3:
                raise ValueError('Triangle requires three arguments: base, height, and side_length')
            base, height, side_length = args
            return 0.5 * base * height
        else:
            raise ValueError(f'Unsupported shape type: {self.shape_type}')
if __name__ == '__main__':
    rectangle = Shape('rectangle')
    print(rectangle.area(4, 5))
    triangle = Shape('triangle')
    print(triangle.area(3, 6, 7))