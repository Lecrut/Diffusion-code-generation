class NumericMultiplier:
    def multiply(self, a: float, b: float) -> float:
        return a * b

if __name__ == '__main__':
    multiplier = NumericMultiplier()
    result1 = multiplier.multiply(3.5, 2.0)
    result2 = multiplier.multiply(4.5, 6.0)
    print(result1)
    print(result2)