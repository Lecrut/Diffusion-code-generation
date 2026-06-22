class Shape:

    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
        if self.shape_type not in ['rectangle', 'triangle']:
            raise ValueError("Unsupported shape type. Please use 'rectangle' or 'triangle'.")

    def area(self, *args):
        if self.shape_type == 'rectangle':
            if len(args) != 2:
                raise ValueError('Rectangle requires two arguments: width and height')
            width, height = args
            return width * height
        elif self.shape_type == 'triangle':
            if len(args) != 2:
                raise ValueError('Triangle requires two arguments: base and height')
            base, height = args
            return 0.5 * base * height
if __name__ == '__main__':
    try:
        rectangle = Shape('rectangle')
        print('Rectangle Area:', rectangle.area(10, 5))
        triangle = Shape('triangle')
        print('Triangle Area:', triangle.area(8, 4))
        invalid_shape = Shape('circle')
    except ValueError as e:
        print(e)