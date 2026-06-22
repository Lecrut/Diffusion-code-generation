class Rectangle:
    def __init__(self, width, height):
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            raise ValueError("Width and height must be numbers")
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rect = Rectangle(5, 3)
    print(rect.perimeter())