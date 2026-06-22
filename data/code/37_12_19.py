class Parallelogram:
    _MINIMUM_DIMENSION = 0

    def __init__(self, base: float, height: float) -> None:
        self._validate_positive_numeric(base, "base")
        self._validate_positive_numeric(height, "height")
        self.base = base
        self.height = height

    @classmethod
    def _validate_positive_numeric(cls, value: float, name: str) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Attribute {name} must be a numeric type.")
        if value <= cls._MINIMUM_DIMENSION:
            raise ValueError(f"Attribute {name} must be strictly positive.")

    def compute_area(self) -> float:
        return self.base * self.height

if __name__ == '__main__':
    shape = Parallelogram(12, 7)
    print(shape.compute_area())