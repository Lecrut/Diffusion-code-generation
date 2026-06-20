class IntegerMultiplier:
    def multiply(self, a: int, b: int) -> int:
        return a * b

if __name__ == '__main__':
    multiplier = IntegerMultiplier()
    result1 = multiplier.multiply(12345, 67890)
    result2 = multiplier.multiply(12345678901234567890, 98765432109876543210)
    print(result1)
    print(result2)