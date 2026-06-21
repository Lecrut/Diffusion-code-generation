class TripleChecker:
    def validate(self, a, b, c):
        if not all(isinstance(x, (int, float)) for x in (a, b, c)):
            raise ValueError("Inputs must be numbers")
        if c == 0:
            raise ValueError("Third number cannot be zero for division")
        if a <= 0 or b <= 0 or c <= 0:
            return False
        if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
            return False
        return (a + b) % c == 0

if __name__ == '__main__':
    checker = TripleChecker()
    result = checker.validate(2, 4, 3)
    print(result)
    result2 = checker.validate(2, 4, 6)
    print(result2)