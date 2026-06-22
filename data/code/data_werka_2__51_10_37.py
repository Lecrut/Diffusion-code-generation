class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def validate_dimensions(width, height):
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            raise ValueError("Width and height must be numbers.")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")

    def perimeter(self):
        return 2 * (self.width + self.height)

def calculate_perimeter(width, height):
    Rectangle.validate_dimensions(width, height)
    rect = Rectangle(width, height)
    return rect.perimeter()

if __name__ == '__main__':
    width = 10.0
    height = 4.5
    perimeter = calculate_perimeter(width, height)
    print(perimeter)