class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    SAMPLE_NUMBER_1 = 9
    SAMPLE_NUMBER_2 = 14
    print(checker.check_odd(SAMPLE_NUMBER_1))
    print(checker.check_odd(SAMPLE_NUMBER_2))