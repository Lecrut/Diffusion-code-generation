class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

if __name__ == '__main__':
    rect = Rectangle(5.0, 3.0)
    print(rect.area())