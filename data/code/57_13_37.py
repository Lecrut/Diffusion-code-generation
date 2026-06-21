class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    SAMPLE_LENGTH = 8.5
    SAMPLE_WIDTH = 1.2
    rectangle = Rectangle(SAMPLE_LENGTH, SAMPLE_WIDTH)
    print(rectangle.area())