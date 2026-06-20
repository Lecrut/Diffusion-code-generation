class TripleChecker:
    def validate(self, a, b, c):
        return all([a > 0, b > 0, c > 0, a % 2 == 0, b % 2 == 0, (a + b) % c == 0])

if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(4, 6, 10))