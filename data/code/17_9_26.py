class NumberChecker:
    def check_parity(self, number):
        if number % 2 == 0:
            return 'Even'
        else:
            return 'Odd'

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [4, 7, 10, 15]
    for value in sample_values:
        print(f"{value} is {checker.check_parity(value)}")