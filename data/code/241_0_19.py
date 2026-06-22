class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def calculate_area(width, height):
        return width * height

if __name__ == '__main__':
    sample_width = 5
    sample_height = 3
    rect = Rectangle(sample_width, sample_height)
    area = Rectangle.calculate_area(rect.width, rect.height)
    print(area)