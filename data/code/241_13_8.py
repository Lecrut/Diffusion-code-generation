class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def area(length, width):
        return length * width

if __name__ == '__main__':
    rect = Rectangle(5, 3)
    print(rect.area())