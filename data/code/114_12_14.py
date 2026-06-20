class PrecisionMultiplier:
    def __init__(self, factor1=3.141592653589793, factor2=2.718281828459045):
        self.factor1 = factor1
        self.factor2 = factor2

    def multiply(self):
        return self.factor1 * self.factor2

if __name__ == '__main__':
    multiplier = PrecisionMultiplier()
    result = multiplier.multiply()
    print(result)