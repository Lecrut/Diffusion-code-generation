class CheckComposite:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _verify_a_positive(self):
        return isinstance(self.a, int) and self.a > 0

    def _verify_b_even(self):
        return isinstance(self.b, int) and self.b % 2 == 0

    def _verify_c_divisible_by_a(self):
        if not self._verify_a_positive():
            return False
        return isinstance(self.c, int) and self.c % self.a == 0

    def run_checks(self):
        first = self._verify_a_positive()
        second = self._verify_b_even()
        third = self._verify_c_divisible_by_a()
        return first and second and third

if __name__ == '__main__':
    evaluator = CheckComposite(5, 10, 25)
    outcome = evaluator.run_checks()
    print(outcome)