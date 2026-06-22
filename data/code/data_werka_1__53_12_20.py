from typing import Final

class SquareCalculator:
    DIAGONAL: Final[float] = 10.0
    
    @staticmethod
    def calculate_side_length(diagonal: float) -> float:
        return diagonal / (2 ** 0.5)

if __name__ == '__main__':
    side_length = SquareCalculator.calculate_side_length(SquareCalculator.DIAGONAL)
    print(side_length)