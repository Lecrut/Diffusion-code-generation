class PrecisionMultiplier:
    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    multiplier = PrecisionMultiplier()
    num1 = 3.141592653589793
    num2 = 2.718281828459045
    result = multiplier.multiply(num1, num2)
    print(result)