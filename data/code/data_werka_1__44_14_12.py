class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def perimeter(self) -> int:
        return 2 * (self.width + self.height)

    def area(self) -> int:
        return self.width * self.height

if __name__ == '__main__':
    rect = Rectangle(9, 2)
    print(rect.perimeter())
    print(rect.area())