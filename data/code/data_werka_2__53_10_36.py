from math import sqrt

class SquareCalculator:
    DIAGONAL_LENGTH = 10.0

    @staticmethod
    def calculate_side_length(diagonal: float) -> float:
        if diagonal <= 0:
            raise ValueError('Diagonal length must be positive.')
        return diagonal / sqrt(2)

if __name__ == '__main__':
    try:
        side_length = SquareCalculator.calculate_side_length(SquareCalculator.DIAGONAL_LENGTH)
        print(f'The side length of the square with diagonal {SquareCalculator.DIAGONAL_LENGTH} is: {side_length}')
    except ValueError as e:
        print(e)