class LargeNumberMultiplier:
    @staticmethod
    def multiply(a, b):
        return a * b

if __name__ == '__main__':
    result = LargeNumberMultiplier.multiply(9223372036854775807, 2)
    print(result)