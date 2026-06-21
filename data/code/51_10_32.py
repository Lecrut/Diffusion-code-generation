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
    print("Perimeter of rect1:", rect1.perimeter())
    print("Area of rect1:", rect1.area())

    rect2 = Rectangle(7.0, 4.0)
    print("Perimeter of rect2:", rect2.perimeter())
    print("Area of rect2:", rect2.area())