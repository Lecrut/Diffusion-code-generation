class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        if not (isinstance(self.width, int) and isinstance(self.height, int)):
            raise ValueError("Width and height must be integers.")
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive integers.")
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    try:
        rect = Rectangle(12, 9)
        print(rect.perimeter())
    except ValueError as e:
        print(e)