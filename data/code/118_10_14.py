class PrecisionMultiplier:
    def multiply(self, a: float, b: float) -> float:
        return a * b

if __name__ == '__main__':
    multiplier = PrecisionMultiplier()
    result1 = multiplier.multiply(3.141592653589793, 2.718281828459045)
    print(result1)
    result2 = multiplier.multiply(1.618033988749895, 0.5772156649015328)
    print(result2)