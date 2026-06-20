class TripleChecker:
    def validate(self, a, b, c):
        if all([a > 0, b > 0, c > 0]):
            if all([a % 2 == 0, b % 2 == 0]):
                if (a + b) % c == 0:
                    return True
        return False

if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(2, 4, 6))
    print(checker.validate(1, 2, 3))
    print(checker.validate(2, 2, 5))
    print(checker.validate(3, 4, 6))