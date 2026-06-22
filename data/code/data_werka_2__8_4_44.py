import math

class ShapeCalculator:
    def __init__(self, shape_type, dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def calculate_area(self):
        if self.shape_type == 'rectangle':
            length, width = self._validate_dimensions(2)
            return length * width
        elif self.shape_type == 'circle':
            radius = self._validate_dimensions(1)[0]
            return math.pi * radius * radius
        else:
            raise ValueError("Unsupported shape type")

    def _validate_dimensions(self, expected_count):
        if len(self.dimensions) != expected_count:
            raise ValueError(f"Expected {expected_count} dimensions for {self.shape_type}, got {len(self.dimensions)}")
        return self.dimensions

if __name__ == '__main__':
    rectangle = ShapeCalculator('rectangle', (10, 5))
    circle = ShapeCalculator('circle', (7,))
    
    print(rectangle.calculate_area())
    print(circle.calculate_area())