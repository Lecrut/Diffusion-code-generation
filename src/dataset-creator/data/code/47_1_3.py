class Multiplier:
    def __init__(self):
        pass
    @staticmethod
    def validate_integer(value, name="value"):
        return isinstance(value, int) and not isinstance(value, bool)
    def multiply(self, num1, num2):
        if not self.validate_integer(num1, "num1"):
            raise TypeError(f"Expected an integer for {name}, got {type(num1).__name__}")
        if not self.validate_integer(num2, "num2"):
            raise TypeError(f"Expected an integer for {name}, got {type(num2).__name__}")
        return num1 * num2
if __name__ == '__main__':
    multiplier = Multiplier()
    value_a = 42
    value_b = -7
    try:
        result = multiplier.multiply(value_a, value_b)
        print(f"Result of {value_a} * {value_b}: {result}")
    except TypeError as e:
        print(f"Error: {e}")