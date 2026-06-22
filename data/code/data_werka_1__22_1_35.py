class NumberChecker:

    def check_odd(self, number):
        return number % 2 != 0
if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.check_odd(1))
    print(checker.check_odd(2))
    print(checker.check_odd(-5))
    print(checker.check_odd(-8))
    print(checker.check_odd(0))