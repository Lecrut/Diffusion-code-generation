class TripleChecker:
    def validate(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return False
        if a % 2 != 0 or b % 2 != 0:
            return False
        if (a + b) % c != 0:
            return False
        return True

if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(2, 4, 6))
    print(checker.validate(1, 2, 3))
    print(checker.validate(2, 2, 5))
    print(checker.validate(3, 4, 6))