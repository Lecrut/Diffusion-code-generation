class NumberChecker:
    EVEN = 0
    ODD = 1

    def check_odd(self, number):
        return number % 2 == self.ODD

if __name__ == '__main__':
    checker = NumberChecker()
    sample_number = 9
    result = checker.check_odd(sample_number)
    print(result)

    another_sample = 12
    print(checker.check_odd(another_sample))