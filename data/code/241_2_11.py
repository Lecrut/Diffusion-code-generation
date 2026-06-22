class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_area(length, width):
        return length * width

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    area_result = Rectangle.calculate_area(rect.length, rect.width)
    print(area_result)