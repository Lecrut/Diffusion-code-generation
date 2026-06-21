class ConditionValidator:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _check_a_positive(self):
        if not isinstance(self.a, (int, float)):
            raise ValueError("Attribute 'a' must be numeric.")
        if self.a <= 0:
            return False
        return True

    def _check_b_even(self):
        if not isinstance(self.b, (int, float)):
            raise ValueError("Attribute 'b' must be numeric.")
        if not isinstance(self.b, int):
            if self.b != int(self.b):
                raise ValueError("Attribute 'b' must be an integer.")
            self.b = int(self.b)
        if self.b % 2 != 0:
            return False
        return True

    def _check_c_divisible_by_a(self):
        if not isinstance(self.c, (int, float)):
            raise ValueError("Attribute 'c' must be numeric.")
        if not isinstance(self.c, int):
            if self.c != int(self.c):
                raise ValueError("Attribute 'c' must be an integer.")
            self.c = int(self.c)
        if self.a == 0:
            return False
        if not isinstance(self.a, int):
            if self.a != int(self.a):
                raise ValueError("Attribute 'a' must be an integer for division check.")
            self.a = int(self.a)
        if self.c % self.a != 0:
            return False
        return True

    def validate(self):
        cond_a = self._check_a_positive()
        if not cond_a:
            return False
        cond_b = self._check_b_even()
        if not cond_b:
            return False
        cond_c = self._check_c_divisible_by_a()
        if not cond_c:
            return False
        return True

if __name__ == '__main__':
    validator = ConditionValidator(2, 4, 8)
    result = validator.validate()
    print(result)