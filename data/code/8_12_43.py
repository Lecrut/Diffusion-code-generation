import math

class AreaCalculator:
    def __init__(self, shape, dimensions, scale_factor):
        self.shape = shape
        self.dimensions = dimensions
        self.scale_factor = scale_factor
    
    def calculate_area(self):
        if self.shape == 'rectangle':
            width, height = self.dimensions
            return width * height
        elif self.shape == 'circle':
            radius = self.dimensions[0]
            return math.pi * (radius ** 2)
        else:
            raise ValueError("Unsupported shape")
    
    def scaled_area(self):
        area = self.calculate_area()
        return area * self.scale_factor

if __name__ == '__main__':
    rectangle_dimensions = (6, 12)
    circle_dimensions = (8,)
    scale_factor = 3.0
    
    rect_calculator = AreaCalculator('rectangle', rectangle_dimensions, scale_factor)
    circ_calculator = AreaCalculator('circle', circle_dimensions, scale_factor)
    
    print(rect_calculator.scaled_area())
    print(circ_calculator.scaled_area())