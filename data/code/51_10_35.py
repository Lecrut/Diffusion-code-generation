class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        if not (isinstance(self.width, (int, float)) and isinstance(self.height, (int, float))):
            raise ValueError("Width and height must be numeric.")
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    try:
        rect = Rectangle(8.5, 4.2)
        print(rect.perimeter())
    except ValueError as e:
        print(f"Error: {e}")