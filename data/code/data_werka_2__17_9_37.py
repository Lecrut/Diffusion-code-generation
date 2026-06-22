class NumberChecker:

    def check_parity(self, number):
        if not isinstance(number, int):
            raise ValueError('Input must be an integer')
        return 'Even' if number % 2 == 0 else 'Odd'
if __name__ == '__main__':
    checker = NumberChecker()
    try:
        print(checker.check_parity(10))
        print(checker.check_parity(15))
        print(checker.check_parity('20'))
    except ValueError as e:
        print(e)