class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def validate_dimensions(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive numbers.")

    def calculate_perimeter(self):
        self.validate_dimensions()
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    width = 8
    height = 15
    rect = Rectangle(width, height)
    perimeter = rect.calculate_perimeter()
    print(perimeter)