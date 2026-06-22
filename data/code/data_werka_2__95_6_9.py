class TripleConditionValidator:
    def __init__(self, a, b, c):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            raise ValueError("Attributes a, b, and c must be numeric.")
        if isinstance(a, float) or isinstance(b, float) or isinstance(c, float):
            if a != int(a) or b != int(b) or c != int(c):
                raise ValueError("Attributes must be integers.")
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def _validate_a_positive(self):
        if self.a <= 0:
            raise ValueError("Attribute 'a' must be positive.")
        return True

    def _validate_b_even(self):
        if self.b % 2 != 0:
            raise ValueError("Attribute 'b' must be even.")
        return True

    def _validate_c_divisible_by_a(self):
        if self.c % self.a != 0:
            raise ValueError("Attribute 'c' must be divisible by 'a'.")
        return True

    def validate_all(self):
        self._validate_a_positive()
        self._validate_b_even()
        self._validate_c_divisible_by_a()
        return {
            'a_positive': True,
            'b_even': True,
            'c_divisible_by_a': True
        }

if __name__ == '__main__':
    validator = TripleConditionValidator(2, 4, 8)
    result = validator.validate_all()
    print(result)