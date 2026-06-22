class NumberChecker:

    def check_odd(self, number):
        if number % 2 == 0:
            return False
        return True
if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.check_odd(5))
    print(checker.check_odd(-2))
    print(checker.check_odd(0))
    print(checker.check_odd(9))
    print(checker.check_odd(-7))