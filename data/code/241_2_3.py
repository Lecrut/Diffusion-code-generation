class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
if __name__ == '__main__':
    rect1 = Rectangle(10, 5)
    print(rect1.area())
    rect2 = Rectangle(7, 3)
    print(rect2.area())