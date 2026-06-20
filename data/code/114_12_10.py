class PrecisionMultiplier:
    def __init__(self):
        self.num1 = 3.141592653589793
        self.num2 = 2.718281828459045

    def multiply(self):
        return self.num1 * self.num2

if __name__ == '__main__':
    multiplier = PrecisionMultiplier()
    result = multiplier.multiply()
    print(result)