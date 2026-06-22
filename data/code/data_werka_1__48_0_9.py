class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @staticmethod
    def calculate_area(base, height):
        return base * height

if __name__ == '__main__':
    base_length = 8
    height_length = 6
    rectangle = Rectangle(base_length, height_length)
    area = Rectangle.calculate_area(rectangle.base, rectangle.height)
    print(area)