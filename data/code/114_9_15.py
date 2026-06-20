class ProductCalculator:
    def multiply(self, num1, num2):
        return num1 * num2

if __name__ == '__main__':
    calculator = ProductCalculator()
    result1 = calculator.multiply(4, 6)
    print(result1)
    result2 = calculator.multiply(7.5, 2)
    print(result2)