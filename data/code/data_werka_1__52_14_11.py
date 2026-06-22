class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def area(length, width):
        return length * width

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 3.0
    rectangle = Rectangle(sample_length, sample_width)
    print(Rectangle.area(rectangle.length, rectangle.width))