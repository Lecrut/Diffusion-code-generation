class LargeNumberMultiplier:
    @staticmethod
    def validate_numbers(a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Both inputs must be integers")
        return True

    @staticmethod
    def multiply(a, b):
        LargeNumberMultiplier.validate_numbers(a, b)
        return a * b

if __name__ == '__main__':
    result = LargeNumberMultiplier.multiply(12345678901234567890, 98765432109876543210)
    print(result)