class TriangleCalculator:
    AREA_FACTOR = 0.5
    MIN_VALUE = 0

    @staticmethod
    def validate_dimensions(base, height):
        if base < TriangleCalculator.MIN_VALUE or height < TriangleCalculator.MIN_VALUE:
            raise ValueError("Dimensions must be non-negative")

    def compute_area(self, base, height):
        self.validate_dimensions(base, height)
        return self.AREA_FACTOR * base * height

if __name__ == '__main__':
    calculator = TriangleCalculator()
    print(calculator.compute_area(10, 5))
    print(calculator.compute_area(0, 10))
    try:
        calculator.compute_area(-2, 5)
    except ValueError as error:
        print(str(error))