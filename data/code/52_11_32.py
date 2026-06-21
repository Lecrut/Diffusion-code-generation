class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    sample_length = 6.0
    sample_width = 4.0
    rect = Rectangle(sample_length, sample_width)
    print(rect.area())