class Rectangle:
    def __init__(self, width, height):
        if not (isinstance(width, int) and isinstance(height, int)):
            raise ValueError("Width and height must be integers.")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    try:
        rect = Rectangle(8, 6)
        print(rect.perimeter())
    except ValueError as e:
        print(e)