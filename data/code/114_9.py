class ProductCalculator:
    def multiply(self, num1, num2):
        return num1 * num2
if __name__ == '__main__':
    calculator = ProductCalculator()
    result = calculator.multiply(5, 10)
    print(result)
    result2 = calculator.multiply(3.5, 2)
    print(result2)