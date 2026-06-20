class RangeChecker:
    MIN_VALUE = 1
    MAX_VALUE = 10

    @staticmethod
    def check_range(value):
        return RangeChecker.MIN_VALUE <= value <= RangeChecker.MAX_VALUE

if __name__ == '__main__':
    sample_values = [0, 5, 10, 15, -5]
    for value in sample_values:
        print(f"Value {value}: {RangeChecker.check_range(value)}")