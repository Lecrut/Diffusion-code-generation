class NumberChecker:

    def check_parity(self, number):
        if number % 2 == 0:
            return 'Even'
        else:
            return 'Odd'
if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.check_parity(4))
    print(checker.check_parity(7))