class Rectangle:
    DEFAULT_LENGTH = 5
    DEFAULT_WIDTH = 3

    @staticmethod
    def calculate_area(length=DEFAULT_LENGTH, width=DEFAULT_WIDTH):
        return length * width

if __name__ == '__main__':
    area1 = Rectangle.calculate_area()
    print(area1)
    area2 = Rectangle.calculate_area(7, 4)
    print(area2)