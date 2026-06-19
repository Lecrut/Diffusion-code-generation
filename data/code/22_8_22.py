class NumberChecker:

    def check_odd(self, number):
        return number % 2 != 0
if __name__ == '__main__':
    checker = NumberChecker()
    result = checker.check_odd(7)
    print(result)
    result = checker.check_odd(10)
    print(result)