class LargeNumberMultiplier:
    @staticmethod
    def multiply(a, b):
        try:
            result = a * b
            return result
        except OverflowError:
            raise ValueError("The multiplication resulted in an overflow")

if __name__ == '__main__':
    try:
        result = LargeNumberMultiplier.multiply(12345678901234567890, 98765432109876543210)
        print(result)
    except ValueError as e:
        print(e)