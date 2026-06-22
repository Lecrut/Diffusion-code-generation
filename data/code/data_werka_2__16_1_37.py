class NumberChecker:

    def check_positivity(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Input must be an integer or float')
        return value > 0
if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.check_positivity(10))
    print(checker.check_positivity(-5))
    print(checker.check_positivity(0))
    print(checker.check_positivity(3.14))