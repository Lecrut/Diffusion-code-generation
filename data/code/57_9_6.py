class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
    
    def area(self, width=None, height=None):
        if self.shape_type == 'rectangle':
            return self.rectangle_area(width, height)
        elif self.shape_type == 'triangle':
            return self.triangle_area(width, height)
        else:
            raise ValueError('Unsupported shape type')
    
    def rectangle_area(self, width, height):
        if width is None or height is None:
            raise ValueError('Rectangle requires both width and height')
        return width * height
    
    def triangle_area(self, base, height):
        if base is None or height is None:
            raise ValueError('Triangle requires both base and height')
        return 0.5 * base * height

if __name__ == '__main__':
    rectangle = Shape('rectangle')
    print("Rectangle Area:", rectangle.area(width=10, height=5))

    triangle = Shape('triangle')
    print("Triangle Area:", triangle.area(base=8, height=6))