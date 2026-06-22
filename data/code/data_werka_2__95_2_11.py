class TripleChecker:
    def __init__(self):
        self.positive_check = lambda x: x > 0
        self.even_check = lambda x: x % 2 == 0

    def validate(self, a, b, c):
        if not all(map(self.positive_check, (a, b, c))):
            return False
        if not (self.even_check(a) and self.even_check(b)):
            return False
        return (a + b) % c == 0

if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(2, 4, 6))
    print(checker.validate(4, 6, 5))
    print(checker.validate(2, 2, 4))
    print(checker.validate(-2, 4, 6))
    print(checker.validate(2, 3, 5))