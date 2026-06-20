class TripleChecker:
    def validate(self, a, b, c):
        MIN_VALUE = 0
        EVEN_CHECK = 2
        if a > MIN_VALUE and b > MIN_VALUE and c > MIN_VALUE:
            if a % EVEN_CHECK == 0 and b % EVEN_CHECK == 0:
                if (a + b) % c == 0:
                    return True
        return False

if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(2, 4, 6))
    print(checker.validate(1, 2, 3))
    print(checker.validate(2, 2, 5))
    print(checker.validate(3, 4, 6))