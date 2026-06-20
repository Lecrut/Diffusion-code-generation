class TripleChecker:

    def validate(self, a, b, c):
        is_positive = all((x > 0 for x in (a, b, c)))
        is_even = all((x % 2 == 0 for x in (a, b)))
        sum_divisible_by_c = (a + b) % c == 0
        return is_positive and is_even and sum_divisible_by_c
if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(4, 6, 2))
    print(checker.validate(3, 5, 8))
    print(checker.validate(10, 20, 5))
    print(checker.validate(7, 9, 1))