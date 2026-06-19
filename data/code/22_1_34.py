class NumberChecker:
    @staticmethod
    def is_odd(n):
        return n % 2 != 0

if __name__ == '__main__':
    sample_values = [4, 7, 0, -3, -4]
    checker = NumberChecker()
    for value in sample_values:
        print(checker.is_odd(value))