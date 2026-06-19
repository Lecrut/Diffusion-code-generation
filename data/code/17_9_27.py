class NumberChecker:

    def check_parity(self, number):
        return 'Even' if number % 2 == 0 else 'Odd'
if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.check_parity(10))
    print(checker.check_parity(7))