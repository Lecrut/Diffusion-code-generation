class SquareCalculator:
    DEFAULT_SIDE = 15

    @staticmethod
    def calculate_area(side):
        return side * side

if __name__ == '__main__':
    side_value = SquareCalculator.DEFAULT_SIDE
    result = SquareCalculator.calculate_area(side_value)
    print(result)