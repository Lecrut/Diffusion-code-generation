class NumberChecker:
    def check_parity(self, number):
        return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [4, 7, 10, 13]
    for value in sample_values:
        print(f"{value} is {checker.check_parity(value)}")