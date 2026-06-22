class NumberChecker:
    def __init__(self, number):
        self.number = number

    def check_parity(self):
        return "Even" if self.number % 2 == 0 else "Odd"

if __name__ == '__main__':
    sample_values = [42, 17, 0, -3]
    for value in sample_values:
        checker = NumberChecker(value)
        print(f"{value} is {checker.check_parity()}")