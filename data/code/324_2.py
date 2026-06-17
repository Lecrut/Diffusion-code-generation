class MultiplicationCalculator:
    def __init__(self):
        self._product = None
    def multiply(self, a, b):
        self._product = a * b
    def get_product(self):
        if self._product is None:
            raise ValueError("Product has not been calculated. Call multiply() first.")
        return self._product
if __name__ == '__main__':
    calculator = MultiplicationCalculator()
    num1 = 12
    num2 = 5
    calculator.multiply(num1, num2)
    result = calculator.get_product()
    print(f"The product of {num1} and {num2} is: {result}")
    calculator2 = MultiplicationCalculator()
    x = 20
    y = 7
    calculator2.multiply(x, y)
    print(f"The product of {x} and {y} is: {calculator2.get_product()}")