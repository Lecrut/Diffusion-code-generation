class NumberChecker:

    def check_parity(self, number):
        if not isinstance(number, int):
            raise ValueError('Input must be an integer')
        return 'Even' if number % 2 == 0 else 'Odd'
if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.check_parity(4))
    print(checker.check_parity(7))