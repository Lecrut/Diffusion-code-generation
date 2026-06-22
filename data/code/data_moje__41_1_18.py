class RhombusGeometry:
    def __init__(self, diagonal_one: float, diagonal_two: float) -> None:
        if diagonal_one <= 0:
            raise ValueError("Diagonal one must be positive.")
        if diagonal_two <= 0:
            raise ValueError("Diagonal two must be positive.")
        self._d1: float = diagonal_one
        self._d2: float = diagonal_two

    def compute_area(self) -> float:
        return (self._d1 * self._d2) * 0.5

if __name__ == '__main__':
    geom = RhombusGeometry(diagonal_one=12.0, diagonal_two=6.0)
    area_result = geom.compute_area()
    print(area_result)