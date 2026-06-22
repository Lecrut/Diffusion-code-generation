class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @staticmethod
    def calculate_area(width, height):
        return width * height

if __name__ == '__main__':
    sample_width = 5
    sample_height = 3
    area = Rectangle.calculate_area(sample_width, sample_height)
    print(area)