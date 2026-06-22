class NumberChecker:
    _POSITIVE_THRESHOLD = 0
    _EVEN_MODULUS = 2
    _DIVISIBLE_BY = 3

    def __init__(self, value):
        self.value = value

    def is_positive(self):
        return self.value > self._POSITIVE_THRESHOLD

    def is_even(self):
        return self.value % self._EVEN_MODULUS == 0

    def is_divisible_by_three(self):
        return self.value % self._DIVISIBLE_BY == 0

    def get_checks(self):
        return (
            self.is_positive(),
            self.is_even(),
            self.is_divisible_by_three()
        )

if __name__ == '__main__':
    test_values = [12, -3, 7, 9, 0]
    for val in test_values:
        checker = NumberChecker(val)
        result = checker.get_checks()
        print(f"Value: {val}, Positive: {result[0]}, Even: {result[1]}, Divisible by 3: {result[2]}")