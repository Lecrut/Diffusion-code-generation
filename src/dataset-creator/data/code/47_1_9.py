class IntegerMultiplier:
    def __init__(self):
        pass
    @staticmethod
    def validate_int(value, name="value"):
        try:
            int(value)
            return True
        except (TypeError, ValueError):
            raise TypeError(f"{name} must be a valid integer.")
    def multiply(self, num1, num2=None):
        self.validate_int(num1, "num1")
        if num2 is None:
            return num1 * 0
        self.validate_int(num2, "num2")
        result = num1 * num2
        return int(result)
if __name__ == '__main__':
    multiplier = IntegerMultiplier()
    val_a = 45
    val_b = -60
    try:
        product = multiplier.multiply(val_a, val_b)
        print(f"Result of {val_a} * {val_b}: {product}")
        try:
            bad_result = multiplier.multiply("45", 10)
        except TypeError as e:
            print(f"Caught expected error for string input: {e}")
    except Exception as exc:
        print(f"Unexpected error occurred: {exc}")