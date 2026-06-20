class OddEvenChecker:
    def is_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = OddEvenChecker()
    print(checker.is_odd(4))
    print(checker.is_odd(7))
    print(checker.is_odd(0))
    print(checker.is_odd(-3))