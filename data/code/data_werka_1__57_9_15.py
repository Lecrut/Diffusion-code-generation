class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
    
    def area(self, *args):
        if self.shape_type == 'rectangle':
            return self._calculate_rectangle_area(*args)
        elif self.shape_type == 'triangle':
            return self._calculate_triangle_area(*args)
        else:
            raise ValueError('Unsupported shape type')
    
    @staticmethod
    def _calculate_rectangle_area(width, height):
        return width * height
    
    @staticmethod
    def _calculate_triangle_area(base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    rectangle = Shape('rectangle')
    triangle = Shape('triangle')

    print("Rectangle Area:", rectangle.area(10, 5))
    print("Triangle Area:", triangle.area(10, 5))