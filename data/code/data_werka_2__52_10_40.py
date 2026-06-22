class Rectangle:
    def __init__(self, length, width):
        self._validate_dimensions(length, width)
        self.length = length
        self.width = width

    @staticmethod
    def _validate_dimensions(length, width):
        if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
            raise TypeError("Length and width must be numbers.")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")

    def calculate_area(self):
        return self.length * self.width

if __name__ == '__main__':
    try:
        rectangle = Rectangle(25, 15)
        area = rectangle.calculate_area()
        print(area)
    except (TypeError, ValueError) as e:
        print(e)