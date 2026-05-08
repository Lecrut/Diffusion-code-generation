class ProductCalculator:
    def multiply(self, a, b):
        return a * b
if __name__ == '__main__':
    calculator = ProductCalculator()
    num1 = 10
    num2 = 5
    result = calculator.multiply(num1, num2)
    print(result)