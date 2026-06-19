class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
    
    @staticmethod
    def rectangle_area(width, height):
        return width * height
    
    @staticmethod
    def triangle_area(base, height):
        return 0.5 * base * height
    
    def area(self, *args):
        if self.shape_type == 'rectangle':
            if len(args) != 2:
                raise ValueError('Rectangle requires two arguments: width and height')
            width, height = args
            return Shape.rectangle_area(width, height)
        elif self.shape_type == 'triangle':
            if len(args) != 2:
                raise ValueError('Triangle requires two arguments: base and height')
            base, height = args
            return Shape.triangle_area(base, height)
        else:
            raise ValueError('Unsupported shape type')

if __name__ == '__main__':
    rectangle = Shape('rectangle')
    print(rectangle.area(10, 5))
    
    triangle = Shape('triangle')
    print(triangle.area(8, 4))