class LargeIntegerMultiplier:
    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    multiplier = LargeIntegerMultiplier()
    result1 = multiplier.multiply(12345678901234567890, 98765432109876543210)
    print(result1)
    result2 = multiplier.multiply(987654321, 123456789)
    print(result2)