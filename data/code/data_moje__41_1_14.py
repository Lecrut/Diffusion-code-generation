class RhombusCalculator:
    DIAGONAL_FACTOR: float = 0.5

    @staticmethod
    def calculate_area(diagonal_one: float, diagonal_two: float) -> float:
        if diagonal_one <= 0 or diagonal_two <= 0:
            raise ValueError("Diagonals must be positive")
        return RhombusCalculator.DIAGONAL_FACTOR * diagonal_one * diagonal_two

if __name__ == '__main__':
    diag_1: float = 12.0
    diag_2: float = 6.0
    area_value: float = RhombusCalculator.calculate_area(diag_1, diag_2)
    print(area_value)