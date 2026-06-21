class PositiveChecker:
    THRESHOLD = 0

    @staticmethod
    def is_positive(number):
        if not isinstance(number, int):
            raise ValueError("Input must be an integer")
        return number > PositiveChecker.THRESHOLD

if __name__ == '__main__':
    sample_values = [15, -3, 0, 8, -7]
    results = {value: PositiveChecker.is_positive(value) for value in sample_values}
    print(results)