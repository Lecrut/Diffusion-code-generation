class TripleChecker:
    POSITIVE_THRESHOLD = 0
    DIVISOR_CHECK = 0

    def validate(self, num1, num2, num3):
        is_positive = num1 > self.POSITIVE_THRESHOLD and num2 > self.POSITIVE_THRESHOLD and num3 > self.POSITIVE_THRESHOLD
        is_even_first = num1 % 2 == self.DIVISOR_CHECK
        is_even_second = num2 % 2 == self.DIVISOR_CHECK
        sum_is_divisible = (num1 + num2) % num3 == self.DIVISOR_CHECK
        return is_positive and is_even_first and is_even_second and sum_is_divisible

if __name__ == '__main__':
    checker = TripleChecker()
    result_one = checker.validate(4, 6, 5)
    result_two = checker.validate(2, 8, 10)
    result_three = checker.validate(-2, 4, 6)
    result_four = checker.validate(3, 5, 4)
    result_five = checker.validate(2, 4, 3)
    print(result_one)
    print(result_two)
    print(result_three)
    print(result_four)
    print(result_five)