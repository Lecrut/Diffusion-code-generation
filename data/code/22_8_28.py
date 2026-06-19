class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_value = 7
    result = checker.check_odd(sample_value)
    print(result)