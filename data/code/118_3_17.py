class SafeMultiplier:
    @staticmethod
    def multiply(a, b):
        return a * b

if __name__ == '__main__':
    multiplier = SafeMultiplier()
    result1 = multiplier.multiply(2**63 - 1, 2)
    result2 = multiplier.multiply(9876543210987654321, 1234567890)
    print(result1)
    print(result2)