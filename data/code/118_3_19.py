class LargeNumberMultiplier:
    @staticmethod
    def multiply(a, b):
        return a * b

if __name__ == '__main__':
    multiplier = LargeNumberMultiplier()
    result = multiplier.multiply(12345678901234567890, 98765432109876543210)
    print(result)