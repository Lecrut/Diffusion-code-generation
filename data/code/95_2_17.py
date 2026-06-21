class TripleChecker:
    def validate(self, a, b, c):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            raise ValueError("Inputs must be numbers")
        if c == 0:
            raise ValueError("Third number cannot be zero for division")
        if a <= 0 or b <= 0 or c <= 0:
            return False
        if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
            return False
        if (a + b) % c != 0:
            return False
        return True

if __name__ == '__main__':
    checker = TripleChecker()
    result = checker.validate(2, 4, 3)
    print(result)