class Rectangle:
    def __init__(self, width, height):
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            raise ValueError("Width and height must be numbers")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    try:
        rect = Rectangle(5, 3)
        perimeter = rect.calculate_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)