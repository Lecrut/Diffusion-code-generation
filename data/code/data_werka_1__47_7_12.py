class Rectangle:
    DEFAULT_LENGTH = 5
    DEFAULT_WIDTH = 3

    @staticmethod
    def calculate_area(length, width):
        return length * width

if __name__ == '__main__':
    area1 = Rectangle.calculate_area(9, 4)
    print(area1)
    area2 = Rectangle.calculate_area(Rectangle.DEFAULT_LENGTH, Rectangle.DEFAULT_WIDTH)
    print(area2)