class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height

if __name__ == '__main__':
    rect = Rectangle(5, 3)
    print(rect.area())