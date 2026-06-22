class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    rect1 = Rectangle(3, 4)
    print(f"Perimeter of rect1: {Rectangle.calculate_perimeter(rect1.length, rect1.width)}")
    rect2 = Rectangle(10.5, 2.5)
    print(f"Perimeter of rect2: {Rectangle.calculate_perimeter(rect2.length, rect2.width)}")