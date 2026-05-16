class NumberChecker:
    def check_negativity(self, value):
        return value < 0
if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.check_negativity(10))
    print(checker.check_negativity(-5))
    print(checker.check_negativity(0))
    print(checker.check_negativity(-1.5))