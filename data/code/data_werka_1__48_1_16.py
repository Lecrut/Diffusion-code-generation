class Shape:
    def __init__(self, length, width=None):
        if length <= 0 or (width is not None and width <= 0):
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width if width is not None else length

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    try:
        square = Shape(5)
        rectangle = Shape(4, 6)
        print("Square Perimeter:", square.perimeter())
        print("Square Area:", square.area())
        print("Rectangle Perimeter:", rectangle.perimeter())
        print("Rectangle Area:", rectangle.area())
    except ValueError as e:
        print(e)