class NumberChecker:

    def check_odd(self, number):
        return number % 2 != 0
if __name__ == '__main__':
    checker = NumberChecker()
    result = checker.check_odd(5)
    print(result)