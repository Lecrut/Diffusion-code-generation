class NumberChecker:
    MAX_VALUE = 100

    @staticmethod
    def is_valid_number(num):
        return num > 0 and num % 2 == 0 and num < NumberChecker.MAX_VALUE

if __name__ == '__main__':
    sample_values = [50, -10, 100, 3.14]
    for value in sample_values:
        print(f"{value}: {NumberChecker.is_valid_number(value)}")