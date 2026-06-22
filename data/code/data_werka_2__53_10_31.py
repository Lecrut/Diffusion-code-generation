from math import sqrt

class SquareCalculator:
    def __init__(self, diagonal_length: float):
        if diagonal_length <= 0:
            raise ValueError('Diagonal length must be positive.')
        self.diagonal_length = diagonal_length

    def calculate_side_length(self) -> float:
        return self.diagonal_length / sqrt(2)

if __name__ == '__main__':
    square_calculator = SquareCalculator(diagonal_length=10.0)
    side_length = square_calculator.calculate_side_length()
    print(f'The side length of the square with diagonal 10.0 is: {side_length}')