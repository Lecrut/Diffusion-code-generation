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
            return 3.14159 * radius * radius
        else:
            return None

if __name__ == '__main__':
    rectangle = ShapeCalculator('rectangle', (5, 10))
    circle = ShapeCalculator('circle', (7,))
    
    print(rectangle.calculate_area())
    print(circle.calculate_area())