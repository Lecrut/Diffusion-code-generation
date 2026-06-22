class TripleChecker:
    POSITIVE_THRESHOLD = 0
    DIVISIBILITY_CHECK = 0

    def validate(self, num1, num2, num3):
        is_positive = num1 > self.POSITIVE_THRESHOLD and num2 > self.POSITIVE_THRESHOLD and num3 > self.POSITIVE_THRESHOLD
        is_even = num1 % 2 == self.DIVISIBILITY_CHECK and num2 % 2 == self.DIVISIBILITY_CHECK
        sum_first_two = num1 + num2
        is_divisible = sum_first_two % num3 == self.DIVISIBILITY_CHECK
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