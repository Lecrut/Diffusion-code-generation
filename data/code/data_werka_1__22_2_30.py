class OddChecker:
    def is_odd(self, number):
        return self._validate_input(number) and number % 2 != 0

    def _validate_input(self, number):
        return isinstance(number, int)

if __name__ == '__main__':
    checker = OddChecker()
    sample_number = 17
    print(checker.is_odd(sample_number))