class SquareCalculator:
    MIN_SIDE_LENGTH = 0

    @staticmethod
    def validate_side_length(side_length):
        if side_length <= SquareCalculator.MIN_SIDE_LENGTH:
            raise ValueError('Side length must be positive')

    @staticmethod
    def calculate_area(side_length):
        SquareCalculator.validate_side_length(side_length)
        return side_length ** 2

if __name__ == '__main__':
    try:
        print(SquareCalculator.calculate_area(6))
        print(SquareCalculator.calculate_area(-5))
    except ValueError as e:
        print(e)