class IntegerMultiplier:
    def __init__(self):
        pass
    @staticmethod
    def validate_integer(value, name="value"):
        return isinstance(value, int) and not isinstance(value, bool)
    def multiply(self, a, b):
        if not self.validate_integer(a, "a"):
            raise TypeError(f"Argument 'a' must be an integer, got {type(a).__name__}")
        if not self.validate_integer(b, "b"):
            raise TypeError(f"Argument 'b' must be an integer, got {type(b).__name__}")
        return a * b
if __name__ == '__main__':
    multiplier = IntegerMultiplier()
    num1 = 42
    num2 = -7
    try:
        result = multiplier.multiply(num1, num2)
        print(f"Result of {num1} * {num2}: {result}")
        num3 = 0
        num4 = 5
        result_zero = multiplier.multiply(num3, num4)
        print(f"Result of {num3} * {num4}: {result_zero}")
    except TypeError as e:
        print(f"Error occurred: {e}")