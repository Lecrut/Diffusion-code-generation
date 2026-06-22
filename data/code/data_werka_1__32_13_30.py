class StringLengthCalculator:
    DEFAULT_TEST_CASES = ["hello", "", "Python is awesome!", "\n\t "]

    @staticmethod
    def calculate_length(s: str) -> int:
        return len(s)

if __name__ == '__main__':
    calculator = StringLengthCalculator()
    for test_case in StringLengthCalculator.DEFAULT_TEST_CASES:
        print(f'"{test_case}" has a length of {calculator.calculate_length(test_case)}')