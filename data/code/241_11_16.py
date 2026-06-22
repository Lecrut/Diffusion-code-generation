class Rectangle:
    def __init__(self, width, height):
        if not self._is_valid_dimension(width) or not self._is_valid_dimension(height):
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    @staticmethod
    def _is_valid_dimension(dimension):
        return isinstance(dimension, (int, float)) and dimension > 0

    def area(self):
        return self.width * self.height

if __name__ == '__main__':
    rect = Rectangle(5, 10)
    print(f"Area of rectangle: {rect.area()}")
    try:
        Rectangle(-5, 10)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        Rectangle(5, 0)
    except ValueError as e:
        print(f"Error caught: {e}")