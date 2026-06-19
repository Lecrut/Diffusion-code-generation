class ShapeCalculator:
    def __init__(self, shape_type, dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions

    def calculate_area(self):
        if self.shape_type == 'rectangle':
            length, width = self.dimensions
            return length * width
        elif self.shape_type == 'circle':
            radius = self.dimensions[0]
            return 3.14159 * (radius ** 2)
        else:
            raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle = ShapeCalculator('rectangle', (5, 3))
    circle = ShapeCalculator('circle', (4,))
    
    print(rectangle.calculate_area())
    print(circle.calculate_area())