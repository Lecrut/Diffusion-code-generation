class EvenChecker:
    EVEN_MODULO = 2

    @staticmethod
    def is_even(n):
        return n % EvenChecker.EVEN_MODULO == 0

if __name__ == '__main__':
    sample_values = [6, 9, 14, 27, 30]
    for value in sample_values:
        print(f"{value} is even: {EvenChecker.is_even(value)}")