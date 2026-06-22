class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [7, 8, 9, 10, 11]
    for value in sample_values:
        print(f"Is {value} odd? {checker.check_odd(value)}")