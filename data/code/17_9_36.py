class NumberChecker:
    def __init__(self):
        self.parity_map = {0: 'Even', 1: 'Odd'}

    def check_parity(self, number):
        return self.parity_map[number % 2]

if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.check_parity(15))
    print(checker.check_parity(28))