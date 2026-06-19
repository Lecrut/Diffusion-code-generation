class NumberChecker:

    def check_odd(self, number):
        return number % 2 != 0
if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.check_odd(4))
    print(checker.check_odd(7))
    print(checker.check_odd(0))
    print(checker.check_odd(-3))
    print(checker.check_odd(-4))