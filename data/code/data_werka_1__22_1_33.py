class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    test_values = [4, 7, 0, -3, -4]
    for value in test_values:
        print(checker.check_odd(value))