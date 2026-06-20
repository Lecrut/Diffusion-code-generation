class LargeNumberMultiplier:
    @staticmethod
    def multiply(a, b):
        return a * b

if __name__ == '__main__':
    multiplier = LargeNumberMultiplier()
    result1 = multiplier.multiply(2**64 - 1, 2)
    print(result1)
    result2 = multiplier.multiply(9876543210987654321, 1234567890123456789)
    print(result2)