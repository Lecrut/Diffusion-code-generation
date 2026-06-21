class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

if __name__ == '__main__':
    rect1 = Rectangle(5.0, 3.0)
    print(rect1.perimeter())
    print(rect1.area())

    rect2 = Rectangle(4.5, 6.0)
    print(rect2.perimeter())
    print(rect2.area())