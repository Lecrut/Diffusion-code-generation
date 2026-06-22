class NumberChecker:
    def __init__(self, number):
        self.number = number

    def check_parity(self):
        return "Even" if self.number % 2 == 0 else "Odd"

if __name__ == '__main__':
    sample_number = 42
    checker = NumberChecker(sample_number)
    print(checker.check_parity())