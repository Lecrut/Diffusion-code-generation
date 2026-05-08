class QuantityCalculator:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2
    def add_numbers(self):
        return self.number1 + self.number2
if __name__ == '__main__':
    calculator = QuantityCalculator(10, 5)
    result = calculator.add_numbers()
    print(result)