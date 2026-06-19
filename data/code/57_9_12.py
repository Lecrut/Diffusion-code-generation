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
            if len(args) != 2:
                raise ValueError('Triangle requires two arguments: base and height')
            base, height = args
            return 0.5 * base * height
        else:
            raise ValueError('Unsupported shape type')

if __name__ == '__main__':
    rectangle = Shape('rectangle')
    triangle = Shape('triangle')
    
    rect_area = rectangle.area(10, 5)
    tri_area = triangle.area(8, 4)
    
    print(f"Rectangle Area: {rect_area}")
    print(f"Triangle Area: {tri_area}")