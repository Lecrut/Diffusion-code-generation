class NumberChecker:
    def check_positivity(self, value):
        return value > 0
if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.check_positivity(10))
    print(checker.check_positivity(-5))
    print(checker.check_positivity(0))
    print(checker.check_positivity(3.14))
    print(checker.check_positivity(-0.001))