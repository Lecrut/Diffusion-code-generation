class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    rect1 = Rectangle(5, 3)
    print(rect1.area())

    rect2 = Rectangle(7, 4)
    print(rect2.area())