from math import sqrt

class SquareCalculator:
    def __init__(self, diagonal: float):
        self.diagonal = diagonal

    def calculate_side_length(self) -> float:
        if self.diagonal <= 0:
            raise ValueError("Diagonal length must be positive")
        return self.diagonal / sqrt(2)

if __name__ == '__main__':
    square_calculator = SquareCalculator(10.0)
    side_length = square_calculator.calculate_side_length()
    print(side_length)