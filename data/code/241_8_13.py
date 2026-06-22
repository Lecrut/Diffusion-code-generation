class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def calculate_area(self) -> int:
        return self.length * self.width

if __name__ == '__main__':
    rect1 = Rectangle(5, 4)
    print(f"Area of rectangle with length 5 and width 4: {rect1.calculate_area()}")

    rect2 = Rectangle(3.5, 2)
    print(f"Area of rectangle with length 3.5 and width 2: {rect2.calculate_area()}")

    rect3 = Rectangle(10, 7.5)
    print(f"Area of rectangle with length 10 and width 7.5: {rect3.calculate_area()}")