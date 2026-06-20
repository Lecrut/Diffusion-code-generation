class LargeNumberMultiplier:
    @staticmethod
    def validate_numbers(a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Both arguments must be integers.")
        return a, b

    @staticmethod
    def multiply(a, b):
        a, b = LargeNumberMultiplier.validate_numbers(a, b)
        return a * b

if __name__ == '__main__':
    result = LargeNumberMultiplier.multiply(12345678901234567890, 98765432109876543210)
    print(result)