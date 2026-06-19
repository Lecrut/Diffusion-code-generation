class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def validate_dimensions(self):
        if not (isinstance(self.length, (int, float)) and isinstance(self.width, (int, float))):
            raise ValueError('Length and width must be numeric values.')
        if self.length <= 0 or self.width <= 0:
            raise ValueError('Length and width must be positive numbers.')

    def calculate_perimeter(self):
        self.validate_dimensions()
        return 2 * (self.length + self.width)
if __name__ == '__main__':
    try:
        rect = Rectangle(10, 5)
        print(rect.calculate_perimeter())
        rect2 = Rectangle(7.5, 3.2)
        print(rect2.calculate_perimeter())
        rect3 = Rectangle(-1, 4)
        print(rect3.calculate_perimeter())
    except ValueError as e:
        print(e)