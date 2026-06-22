class SquareCalculator:
    OPERATION_MULTIPLY = 1

    @staticmethod
    def compute_area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    calculator = SquareCalculator()
    print(calculator.compute_area(4))
    print(calculator.compute_area(7))