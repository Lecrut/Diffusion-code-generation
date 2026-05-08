class QuantityCalculator:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2
    def add_quantities(self):
        result = self.number1 + self.number2
        return result
if __name__ == '__main__':
    calculator = QuantityCalculator(10, 5)
    sum_result = calculator.add_quantities()
    print(sum_result)