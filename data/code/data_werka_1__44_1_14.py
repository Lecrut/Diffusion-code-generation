class Rectangle:
    def __init__(self, dimensions):
        self.length = self.validate_dimension(dimensions['length'])
        self.width = self.validate_dimension(dimensions['width'])
    
    @staticmethod
    def validate_dimension(value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return value
    
    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    sample_dimensions = {'length': 9, 'width': 2}
    rect = Rectangle(sample_dimensions)
    print(rect.perimeter())