class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def validate_dimensions(dimensions):
        if len(dimensions) != 2:
            raise ValueError("The dimensions list must contain exactly two elements.")
        length, width = dimensions
        if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
            raise TypeError("Both dimensions must be numbers.")
        if length <= 0 or width <= 0:
            raise ValueError("Both dimensions must be positive numbers.")

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    sample_dimensions = [7, 4]
    try:
        Rectangle.validate_dimensions(sample_dimensions)
        rectangle = Rectangle(*sample_dimensions)
        perimeter = rectangle.calculate_perimeter()
        print(perimeter)
    except Exception as e:
        print(e)