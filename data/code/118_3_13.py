class LargeNumberMultiplier:
    @staticmethod
    def multiply(a, b):
        return a * b

if __name__ == '__main__':
    multiplier = LargeNumberMultiplier()
    result1 = multiplier.multiply(2**30, 2**30)
    result2 = multiplier.multiply(999999999999999999, 999999999999999999)
    print(result1)
    print(result2)