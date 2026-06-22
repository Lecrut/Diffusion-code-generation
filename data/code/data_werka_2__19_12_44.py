class EvenChecker:
    DIVISOR = 2

    @staticmethod
    def is_even(n):
        return n % EvenChecker.DIVISOR == 0

if __name__ == '__main__':
    test_values = [-11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11]
    even_results = {value: EvenChecker.is_even(value) for value in test_values}
    print(even_results)