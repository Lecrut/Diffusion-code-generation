class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def validate_dimensions(self):
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return True

    def perimeter(self):
        if not self.validate_dimensions():
            return None
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    sample_length = 8
    sample_width = 5
    rect = Rectangle(sample_length, sample_width)
    
    try:
        print(rect.perimeter())
    except ValueError as e:
        print(e)