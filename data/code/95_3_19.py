class NumberChecker:
    MIN_VALUE = 0
    MAX_VALUE = 100

    @staticmethod
    def is_valid_number(num):
        return num > NumberChecker.MIN_VALUE and num % 2 == 0 and num < NumberChecker.MAX_VALUE

if __name__ == '__main__':
    sample_value = 42
    print(NumberChecker.is_valid_number(sample_value))