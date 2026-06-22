class NumberChecker:
    def __init__(self, number):
        self.number = number

    def check_parity(self):
        return "Even" if self.number % 2 == 0 else "Odd"

if __name__ == '__main__':
    sample_values = [42, 7, 15, 28]
    for value in sample_values:
        checker = NumberChecker(value)
        result = checker.check_parity()
        print(f"The number {value} is {result}.")