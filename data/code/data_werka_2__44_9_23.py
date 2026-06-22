class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def validate_dimensions(length, width):
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError("Both dimensions must be numeric.")
        if length <= 0 or width <= 0:
            raise ValueError("Dimensions must be positive numbers.")

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        length = 8.5
        width = 3.4
        Rectangle.validate_dimensions(length, width)
        rectangle = Rectangle(length, width)
        print(f"Length: {rectangle.length}")
        print(f"Width: {rectangle.width}")
        print(f"Perimeter: {rectangle.calculate_perimeter()}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")