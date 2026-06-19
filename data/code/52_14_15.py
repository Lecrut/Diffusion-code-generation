class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
if __name__ == '__main__':
    rect = Rectangle(length=10, width=5)
    print(rect.area())