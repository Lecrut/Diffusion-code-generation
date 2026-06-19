class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def calculate_perimeter(self) -> float:
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect1 = Rectangle(8.0, 6.0)
    perimeter1 = rect1.calculate_perimeter()
    print(perimeter1)

    rect2 = Rectangle(15.5, 4.2)
    perimeter2 = rect2.calculate_perimeter()
    print(perimeter2)