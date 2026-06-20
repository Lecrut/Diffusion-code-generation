class TripleChecker:
    def validate(self, a, b, c):
        return a > 0 and b > 0 and c > 0 and a % 2 == 0 and b % 2 == 0 and (a + b) % c == 0

if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(4, 6, 10))