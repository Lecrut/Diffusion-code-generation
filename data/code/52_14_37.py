SQUARE_DIMENSIONS = {'side_length': 0}

class SquareCalculator:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def calculate_area(self):
        side_length = self.dimensions.get('side_length', 0)
        if not isinstance(side_length, (int, float)):
            raise ValueError("Side length must be a number")
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        return side_length ** 2

if __name__ == '__main__':
    sample_side_length = 6
    SQUARE_DIMENSIONS['side_length'] = sample_side_length
    calculator = SquareCalculator(SQUARE_DIMENSIONS)
    area = calculator.calculate_area()
    print(area)

    another_sample_side_length = 10
    SQUARE_DIMENSIONS['side_length'] = another_sample_side_length
    another_calculator = SquareCalculator(SQUARE_DIMENSIONS)
    another_area = another_calculator.calculate_area()
    print(another_area)