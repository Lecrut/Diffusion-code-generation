WIDTH_LIMIT = 1e9
HEIGHT_LIMIT = 1e9

class RectangleGeometry:
    def __init__(self, width, height):
        self._validate(width)
        self._validate(height)
        self.width = width
        self.height = height

    def _validate(self, value):
        if isinstance(value, bool):
            raise TypeError("Dimensions must be numeric types, not bool.")
        if not isinstance(value, (int, float)):
            raise TypeError(f"Dimension must be int or float, got {type(value).__name__}.")
        if value < 0:
            raise ValueError("Dimensions must be non-negative.")

    def calculate_area(self):
        w = self.width
        h = self.height
        if w > WIDTH_LIMIT or h > HEIGHT_LIMIT:
            raise OverflowError("Dimensions exceed maximum allowed size.")
        return w * h

if __name__ == '__main__':
    rect = RectangleGeometry(10, 20)
    area = rect.calculate_area()
    print(area)