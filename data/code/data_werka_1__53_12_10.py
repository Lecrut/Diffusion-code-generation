from math import sqrt

class SquareCalculator:
    def __init__(self, diagonal: float):
        self.diagonal = diagonal

    def calculate_side_length(self) -> float:
        return self.diagonal / sqrt(2)

if __name__ == '__main__':
    calculator = SquareCalculator(10.0)
    side_length = calculator.calculate_side_length()
    print(side_length)