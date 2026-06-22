class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
    
    def area(self, *args):
        if len(args) != 2:
            raise ValueError('Both width and height/base are required')
        
        width, height = args
        
        if self.shape_type == 'rectangle':
            return width * height
        elif self.shape_type == 'triangle':
            return 0.5 * width * height
        else:
            raise ValueError('Unsupported shape type')

if __name__ == '__main__':
    rectangle = Shape('rectangle')
    triangle = Shape('triangle')
    
    print("Rectangle area:", rectangle.area(10, 5))
    print("Triangle area:", triangle.area(10, 5))