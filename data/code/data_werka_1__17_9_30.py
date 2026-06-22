class NumberChecker:
    def check_parity(self, number):
        if number % 2 == 0:
            return 'Even'
        else:
            return 'Odd'

if __name__ == '__main__':
    checker = NumberChecker()
    sample_value = 42
    result = checker.check_parity(sample_value)
    print(result)