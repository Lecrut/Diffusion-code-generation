class TripleChecker:
    def validate(self, a, b, c):
        if all(x > 0 for x in [a, b, c]) and all(x % 2 == 0 for x in [a, b]):
            return (a + b) % c == 0
        return False

if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(2, 4, 6))
    print(checker.validate(1, 2, 3))
    print(checker.validate(2, 2, 5))
    print(checker.validate(3, 4, 6))