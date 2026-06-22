class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def calculate_perimeter(self) -> float:
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect = Rectangle(10.0, 5.0)
    print(rect.calculate_perimeter())