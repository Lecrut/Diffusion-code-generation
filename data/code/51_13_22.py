class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    sample_values = {
        'length': 7,
        'width': 4
    }
    rect = Rectangle(sample_values['length'], sample_values['width'])
    print(rect.perimeter())