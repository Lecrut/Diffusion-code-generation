class TripleChecker:
    def validate(self, a, b, c):
        if a > 0 and b > 0 and c > 0:
            if a % 2 == 0 and b % 2 == 0:
                if (a + b) % c == 0:
                    return True
        return False
if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(2, 4, 6))
    print(checker.validate(1, 2, 3))
    print(checker.validate(2, 2, 5))
    print(checker.validate(3, 4, 6))
    print(checker.validate(10, 20, 30))
    print(checker.validate(1, 2, 4))