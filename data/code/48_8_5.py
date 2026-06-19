class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @staticmethod
    def calculate_area(base, height):
        return base * height

if __name__ == '__main__':
    base_length = 6.0
    height_length = 4.5
    rectangle = Rectangle(base_length, height_length)
    area = Rectangle.calculate_area(base_length, height_length)
    print(area)