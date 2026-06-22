import math

class Shape:

    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions

    def area(self):
        if self.shape_type == 'rectangle':
            length = self.dimensions.get('length')
            width = self.dimensions.get('width')
            if length is None or width is None:
                raise ValueError('Rectangle requires both length and width.')
            return length * width
        elif self.shape_type == 'circle':
            radius = self.dimensions.get('radius')
            if radius is None:
                raise ValueError('Circle requires a radius.')
            return math.pi * radius ** 2
        else:
            raise ValueError(f'Unsupported shape type: {self.shape_type}')
if __name__ == '__main__':
    rect_length = 5
    rect_width = 3
    rectangle = Shape('rectangle', length=rect_length, width=rect_width)
    print(f'Area of the rectangle: {rectangle.area()}')
    circle_radius = 4
    circle = Shape('circle', radius=circle_radius)
    print(f'Area of the circle: {circle.area()}')