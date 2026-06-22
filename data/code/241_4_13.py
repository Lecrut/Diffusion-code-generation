class Rectangle:
    @staticmethod
    def calculate_area(width: int, height: int) -> int:
        return width * height

if __name__ == '__main__':
    area = Rectangle.calculate_area(5, 3)
    print(area)