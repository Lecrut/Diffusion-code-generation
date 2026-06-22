class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def area(self) -> int:
        return self.length * self.width

if __name__ == '__main__':
    rect1 = Rectangle(5, 4)
    print(f"Area of 5 and 4: {rect1.area()}")

    rect2 = Rectangle(3, 2)
    print(f"Area of 3 and 2: {rect2.area()}")

    rect3 = Rectangle(10, 7)
    print(f"Area of 10 and 7: {rect3.area()}")