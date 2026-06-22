class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

    def area(self) -> int:
        return self.multiply(self.length, self.width)

if __name__ == '__main__':
    rect1 = Rectangle(5, 4)
    print(f"Area of rectangle with length 5 and width 4: {rect1.area()}")

    rect2 = Rectangle(3, 6)
    print(f"Area of rectangle with length 3 and width 6: {rect2.area()}")