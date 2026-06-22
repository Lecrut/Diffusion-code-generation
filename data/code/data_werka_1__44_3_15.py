class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def validate_dimensions(self):
        if not isinstance(self.length, (int, float)) or not isinstance(self.width, (int, float)):
            raise TypeError("Both dimensions must be numbers.")
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Both dimensions must be positive numbers.")

    def calculate_perimeter(self):
        self.validate_dimensions()
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        sample_rectangle = Rectangle(10, 4)
        perimeter = sample_rectangle.calculate_perimeter()
        print(perimeter)
    except Exception as e:
        print(e)