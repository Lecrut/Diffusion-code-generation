class TripleChecker:
    def validate(self, a, b, c):
        is_positive = a > 0 and b > 0 and c > 0
        is_even = a % 2 == 0 and b % 2 == 0
        sum_val = a + b
        is_divisible = sum_val % c == 0
        return is_positive and is_even and is_divisible

if __name__ == '__main__':
    checker = TripleChecker()
    result1 = checker.validate(4, 6, 5)
    result2 = checker.validate(2, 8, 5)
    result3 = checker.validate(1, 2, 3)
    result4 = checker.validate(10, 20, 15)
    print(result1)
    print(result2)
    print(result3)
    print(result4)