class FloatMultiplier:
    def multiply(self, a: float, b: float) -> float:
        return a * b

if __name__ == '__main__':
    multiplier = FloatMultiplier()
    result1 = multiplier.multiply(3.141592653589793, 2.718281828459045)
    result2 = multiplier.multiply(1.4142135623730951, 2.718281828459045)
    print(result1)
    print(result2)