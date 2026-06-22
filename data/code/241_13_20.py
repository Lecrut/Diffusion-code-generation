class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    rect = Rectangle(5, 3)
    print(f"Length: {rect.length}, Width: {rect.width}, Area: {rect.area()}")