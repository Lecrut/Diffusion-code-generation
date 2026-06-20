class ConditionChecker:
    def check_even_and_positive(self, n):
        return n > 0 and (n & 1) == 0

if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_even_and_positive(4))
    print(checker.check_even_and_positive(-2))
    print(checker.check_even_and_positive(0))
    print(checker.check_even_and_positive(3))