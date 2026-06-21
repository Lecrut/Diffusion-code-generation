class SquareCalculator:
    def __init__(self):
        self._side_length = None

    @property
    def side_length(self):
        return self._side_length

    @side_length.setter
    def side_length(self, value):
        if value <= 0:
            raise ValueError('Side length must be positive')
        self._side_length = value

    def calculate_area(self):
        return self._side_length ** 2

if __name__ == '__main__':
    calculator = SquareCalculator()
    try:
        calculator.side_length = 6
        print(calculator.calculate_area())
        calculator.side_length = -5
        print(calculator.calculate_area())
    except ValueError as e:
        print(e)