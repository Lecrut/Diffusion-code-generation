class IntegerMultiplier:
    def __init__(self):
        pass
    def validate_int(self, value) -> bool:
        return isinstance(value, int) and not isinstance(value, type(True))
    def multiply(self, a: int, b: int) -> int:
        if self.validate_int(a) and self.validate_int(b):
            return a * b
        else:
            raise TypeError("Both arguments must be integers.")
    def multiply_safe(self, a: int | float = None, b: int | float = None) -> int | None:
        default_a = a if self.validate_int(a) else 0
        default_b = b if self.validate_int(b) else 1
        return self.multiply(default_a, default_b)
if __name__ == '__main__':
    multiplier = IntegerMultiplier()
    num_1: int = 42
    num_2: int = -7
    try:
        result = multiplier.multiply(num_1, num_2)
        print(f"Result of {num_1} * {num_2}: {result}")
    except TypeError as e:
        print(f"Error during multiplication: {e}")