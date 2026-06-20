class NegativeChecker:
    def is_negative(self, number):
        return number < 0

if __name__ == '__main__':
    checker = NegativeChecker()
    print(checker.is_negative(-5.0))
    print(checker.is_negative(0))
    print(checker.is_negative(3.14))