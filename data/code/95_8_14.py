class NumberChecker:
    MAX_LIMIT = 100

    @staticmethod
    def is_positive_even_and_less_than_limit(number):
        return number > 0 and number % 2 == 0 and number < NumberChecker.MAX_LIMIT

if __name__ == '__main__':
    print(NumberChecker.is_positive_even_and_less_than_limit(34))
    print(NumberChecker.is_positive_even_and_less_than_limit(56))
    print(NumberChecker.is_positive_even_and_less_than_limit(102))
    print(NumberChecker.is_positive_even_and_less_than_limit(-4))