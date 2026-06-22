class TrapezoidCalculator:
    def __init__(self, base1: float, base2: float, height: float) -> None:
        if not isinstance(base1, (int, float)) or not isinstance(base2, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("All dimensions must be numeric")
        if base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("Bases and height must be strictly positive")
        self._base1 = float(base1)
        self._base2 = float(base2)
        self._height = float(height)

    def get_area(self) -> float:
        return 0.5 * (self._base1 + self._base2) * self._height

    def get_perimeter_estimate(self, side1: float = 1.0, side2: float = 1.0) -> float:
        return self._base1 + self._base2 + side1 + side2

if __name__ == '__main__':
    sample_base1 = 8.5
    sample_base2 = 12.5
    sample_height = 4.0
    calculator = TrapezoidCalculator(sample_base1, sample_base2, sample_height)
    area_result = calculator.get_area()
    print(area_result)