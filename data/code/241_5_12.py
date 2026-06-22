class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

if __name__ == '__main__':
    rect1 = Rectangle(5.0, 10.0)
    rect2 = Rectangle(3.0, 7.0)

    print("Area of rectangle1:", rect1.area())
    print("Area of rectangle2:", rect2.area())