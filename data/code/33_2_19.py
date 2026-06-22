class TriangleAreaCalculator:
    _FORMULA_COEFFICIENT = 0.5

    def __init__(self, base: float, height: float) -> None:
        self._base = base
        self._height = height

    @staticmethod
    def _validate_dimensions(base: float, height: float) -> None:
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers")

    def get_area(self) -> float:
        self._validate_dimensions(self._base, self._height)
        return self._FORMULA_COEFFICIENT * self._base * self._height

if __name__ == '__main__':
    sample_base = 8.5
    sample_height = 12.0
    instance = TriangleAreaCalculator(sample_base, sample_height)
    print(instance.get_area())