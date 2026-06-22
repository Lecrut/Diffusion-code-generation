class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @staticmethod
    def calculate_area(width: int, height: int) -> int:
        return width * height

if __name__ == '__main__':
    rect = Rectangle(5, 3)
    area = Rectangle.calculate_area(rect.width, rect.height)
    print(area)