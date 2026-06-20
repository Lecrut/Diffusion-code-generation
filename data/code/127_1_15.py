class NumberChecker:
    @staticmethod
    def is_odd(number):
        return number % 2 != 0

if __name__ == '__main__':
    sample_values = [-3, -2, 0, 1, 4]
    for value in sample_values:
        print(f"{value}: {NumberChecker.is_odd(value)}")