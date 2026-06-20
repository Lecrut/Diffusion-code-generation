class NumberChecker:
    MAX_VALUE = 100

    @staticmethod
    def is_positive_even_and_less_than_max(number):
        return number > 0 and number % 2 == 0 and number < NumberChecker.MAX_VALUE

if __name__ == '__main__':
    sample_numbers = [3, 5, 2, 1]
    for num in sample_numbers:
        result = NumberChecker.is_positive_even_and_less_than_max(num)
        print(f"Number {num}: {'is' if result else 'is not'} positive, even, and less than 100")