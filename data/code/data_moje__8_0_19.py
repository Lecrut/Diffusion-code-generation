class Rectangle:
    def __init__(self, width, height):
        self._width = self._validate_dimension(width, "width")
        self._height = self._validate_dimension(height, "height")

    @staticmethod
    def _validate_dimension(value, name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"The {name} must be a numeric value.")
        if value < 0:
            raise ValueError(f"The {name} cannot be negative.")
        return float(value)

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2 * (self._width + self._height)

if __name__ == '__main__':
    sample_width = 12.5
    sample_height = 7.2
    rect = Rectangle(sample_width, sample_height)
    calculated_area = rect.get_area()
    print(calculated_area)