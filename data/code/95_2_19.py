class TripleChecker:
    POSITIVE_THRESHOLD = 0
    DIVISIBILITY_CHECK = 0

    def validate(self, a: int, b: int, c: int) -> bool:
        if a <= self.POSITIVE_THRESHOLD or b <= self.POSITIVE_THRESHOLD or c <= self.POSITIVE_THRESHOLD:
            return False
        if a % 2 != 0 or b % 2 != 0:
            return False
        if (a + b) % c != self.DIVISIBILITY_CHECK:
            return False
        return True

if __name__ == '__main__':
    checker = TripleChecker()
    result1 = checker.validate(4, 6, 5)
    print(result1)
    result2 = checker.validate(2, 2, 4)
    print(result2)
    result3 = checker.validate(-1, 2, 3)
    print(result3)
    result4 = checker.validate(3, 5, 4)
    print(result4)
    result5 = checker.validate(10, 20, 5)
    print(result5)