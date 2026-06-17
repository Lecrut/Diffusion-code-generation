class MultiplicationCalculator:
    def __init__(self):
        self._product = None
    def multiply(self, a, b):
        self._product = a * b
        return self._product
if __name__ == '__main__':
    calculator = MultiplicationCalculator()
    num1 = 12
    num2 = 5
    result = calculator.multiply(num1, num2)
    print(f"The product of {num1} and {num2} is: {result}")