class RhombusGeometry:
    def __init__(self, diagonal_primary: float, diagonal_secondary: float) -> None:
        self._diag1: float = diagonal_primary
        self._diag2: float = diagonal_secondary

    def calculate_area(self) -> float:
        half_product: float = self._diag1 * self._diag2
        return half_product / 2.0

if __name__ == '__main__':
    r: RhombusGeometry = RhombusGeometry(diagonal_primary=12.5, diagonal_secondary=7.0)
    result: float = r.calculate_area()
    print(result)