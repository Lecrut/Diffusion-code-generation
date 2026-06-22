class Rectangle:
    def __init__(self, length, width):
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise ValueError("Length and width must be numbers")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.area())