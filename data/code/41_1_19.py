class RhombusGeometry:
    DIAGONAL_FACTOR: float = 0.5

    @staticmethod
    def _validate_positive(value: float) -> None:
        if value <= 0:
            raise ValueError("Diagonals must be positive")

    def compute_area(self, d1: float, d2: float) -> float:
        self._validate_positive(d1)
        self._validate_positive(d2)
        return self._calculate(d1, d2)

    @staticmethod
    def _calculate(d1: float, d2: float) -> float:
        return RhombusGeometry.DIAGONAL_FACTOR * d1 * d2

if __name__ == '__main__':
    instance = RhombusGeometry()
    diag_a: float = 12.0
    diag_b: float = 9.0
    computed_area: float = instance.compute_area(diag_a, diag_b)
    print(computed_area)