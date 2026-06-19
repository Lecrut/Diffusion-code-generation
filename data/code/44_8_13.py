class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def validate_dimensions(self):
        if not isinstance(self.length, (int, float)) or not isinstance(self.width, (int, float)):
            raise TypeError("Length and width must be numbers.")
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Length and width must be positive numbers.")

    def get_perimeter(self):
        self.validate_dimensions()
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        rect = Rectangle(9, 3)
        print(rect.get_perimeter())
    except Exception as e:
        print(e)