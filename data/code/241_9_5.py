class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_area(length, width):
        return length * width

if __name__ == '__main__':
    rectangle = Rectangle(5, 3)
    area = Rectangle.calculate_area(rectangle.length, rectangle.width)
    print(area)