class NumberChecker:
    def check_odd(self, number):
        if number % 2 == 0:
            return False
        return True

if __name__ == '__main__':
    checker = NumberChecker()
    sample_number = 15
    print(checker.check_odd(sample_number))
    another_sample = 8
    print(checker.check_odd(another_sample))