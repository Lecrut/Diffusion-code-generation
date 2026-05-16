class ProductCalculator:
    def multiply(self, num1, num2):
        return num1 * num2
if __name__ == '__main__':
    calculator = ProductCalculator()
    result = calculator.multiply(5, 10)
    print(result)