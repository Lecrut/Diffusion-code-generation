class Multiplier:
    def __init__(self):
        pass
    @staticmethod
    def validate_integer(value, name="value"):
        if isinstance(value, float) or value < 0 or value > 1_000_000:
            raise ValueError(f"{name} must be a non-negative integer <= 1,000,000.")
        return True
    def multiply(self, num1, num2):
        self.validate_integer(num1, "num1")
        self.validate_integer(num2, "num2")
        return int(num1 * num2)
if __name__ == '__main__':
    multiplier = Multiplier()
    sample_value_1 = 42
    sample_value_2 = 50
    try:
        result = multiplier.multiply(sample_value_1, sample_value_2)
        print(f"Result of {sample_value_1} * {sample_value_2}: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error occurred: {e}")