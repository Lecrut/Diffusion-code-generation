class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def calculate_area(width, height):
        return width * height

if __name__ == '__main__':
    rect_width = 5
    rect_height = 3
    area = Rectangle.calculate_area(rect_width, rect_height)
    print(area)