class CompositeValidator:
    def __init__(self, a, b, c):
        self._validate_inputs(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def _validate_inputs(a, b, c):
        if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
            raise ValueError("Inputs must be integers.")
        if a <= 0:
            raise ValueError("Attribute 'a' must be positive.")
        if b % 2 != 0:
            raise ValueError("Attribute 'b' must be even.")
        if a == 0:
            raise ValueError("Division by zero is not allowed.")
        if c % a != 0:
            raise ValueError("Attribute 'c' must be divisible by 'a'.")

    def check_conditions(self):
        return self.a > 0 and self.b % 2 == 0 and self.c % self.a == 0

if __name__ == '__main__':
    validator = CompositeValidator(2, 4, 8)
    result = validator.check_conditions()
    print(result)