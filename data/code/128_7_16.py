class NumberChecker:
    def check_negative(self, number):
        return number < 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [-5, 3, -10, 7, 0]
    for value in sample_values:
        if checker.check_negative(value):
            print(f"{value} is negative.")
        else:
            print(f"{value} is not negative.")