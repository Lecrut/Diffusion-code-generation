class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    try:
        rect = Rectangle(5, 3)
        print(rect.area())
    except ValueError as e:
        print(e)