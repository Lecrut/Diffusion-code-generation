class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rect = Rectangle(4.5, 6.2)
    print(rect.area())
    print(rect.perimeter())