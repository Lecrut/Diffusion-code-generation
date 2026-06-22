class Rectangle:
    def __init__(self, length, width):
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise ValueError("Length and width must be numbers.")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    try:
        rectangle = Rectangle(18, 6)
        print(rectangle.area())
    except ValueError as e:
        print(e)