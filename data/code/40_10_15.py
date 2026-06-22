class BoxSurfaceCalculator:
    def __init__(self, length, width, height):
        self._validate_dimension("length", length)
        self._validate_dimension("width", width)
        self._validate_dimension("height", height)
        self.length = length
        self.width = width
        self.height = height

    def _validate_dimension(self, name, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number")
        if value <= 0:
            raise ValueError(f"{name} must be greater than zero")

    def calculate(self):
        term1 = self.length * self.width
        term2 = self.width * self.height
        term3 = self.height * self.length
        return 2 * (term1 + term2 + term3)

if __name__ == '__main__':
    box = BoxSurfaceCalculator(10, 5, 3)
    print(box.calculate())