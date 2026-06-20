class LargeNumberMultiplier:
    @staticmethod
    def multiply(a, b):
        return a * b

if __name__ == '__main__':
    result = LargeNumberMultiplier.multiply(2**64 - 1, 2)
    print(result)