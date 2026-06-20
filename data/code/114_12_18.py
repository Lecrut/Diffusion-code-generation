class PrecisionMultiplier:
    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    multiplier = PrecisionMultiplier()
    result = multiplier.multiply(3.141592653589793, 2.718281828459045)
    print(result)