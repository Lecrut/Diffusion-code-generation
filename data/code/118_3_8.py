class LargeNumberMultiplier:
    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

if __name__ == '__main__':
    result = LargeNumberMultiplier.multiply(12345678901234567890, 98765432109876543210)
    print(result)