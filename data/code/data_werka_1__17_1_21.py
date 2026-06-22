class NumberChecker:
    def __init__(self, number):
        self.number = number

    def check_parity(self):
        return "Even" if self.number % 2 == 0 else "Odd"

if __name__ == '__main__':
    checker1 = NumberChecker(4)
    print(checker1.check_parity())

    checker2 = NumberChecker(7)
    print(checker2.check_parity())