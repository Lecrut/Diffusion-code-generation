class NumberChecker:
    POSITIVE_THRESHOLD = 0

    @staticmethod
    def is_positive(number):
        return number > NumberChecker.POSITIVE_THRESHOLD

if __name__ == '__main__':
    sample_values = [15, -3, 0, 8, -7]
    results = {value: NumberChecker.is_positive(value) for value in sample_values}
    print(results)