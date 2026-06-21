from typing import Final

class SquareCalculator:
    def __init__(self, side_length: float):
        self.side_length = side_length

    def compute_area(self) -> float:
        return self._calculate_area()

    def _calculate_area(self) -> float:
        if self.side_length < 0:
            raise ValueError("Side length cannot be negative")
        return self.side_length * self.side_length

if __name__ == '__main__':
    DEFAULT_SIDE_LENGTH: Final[float] = 5.0
    calculator_instance = SquareCalculator(DEFAULT_SIDE_LENGTH)
    area = calculator_instance.compute_area()
    print(area)