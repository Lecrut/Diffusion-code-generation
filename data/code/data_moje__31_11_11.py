class SquareCalculator:
    _POWER = 2

    @staticmethod
    def calculate_area(side_length):
        return side_length ** SquareCalculator._POWER

if __name__ == '__main__':
    side = 15
    result = SquareCalculator.calculate_area(side)
    print(result)