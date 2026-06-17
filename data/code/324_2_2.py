class MultiplicationCalculator:
    def __init__(self):
        self._result = None
    def multiply(self, a, b):
        self._result = a * b
        return self._result
if __name__ == '__main__':
    calculator = MultiplicationCalculator()
    num1 = 12
    num2 = 5
    product = calculator.multiply(num1, num2)
    print(f"The product of {num1} and {num2} is: {product}")
    num3 = 25
    num4 = 4
    product2 = calculator.multiply(num3, num4)
    print(f"The product of {num3} and {num4} is: {product2}")